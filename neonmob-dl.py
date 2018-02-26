#!/usr/bin/env python3

# Glossary:
# stm: statement
# res: result

import requests
import re
import json
from bs4 import BeautifulSoup
import os
import argparse
import io


class Pass:
    pass


SCHEME = "https://"
DOMAIN = "www.neonmob.com"
BASE_URL = SCHEME + DOMAIN
CLOUDFRONT_PREFIX = "https:"

API = Pass()
API.setts = '/api/setts/{}/'
API.piece_names = '/api/sets/{}/piece-names/'
API.piece_details = '/api/users/{}/piece/{}/detail/'

API.owned_setts = 'https://napi.neonmob.com/user/{}/owned-setts-metrics/'

class NeonmobSett:
    setts = None
    piece_names = None

    def endpoint(self, api_url, target="sett", **kwargs):
        if target == 'sett':
            url = BASE_URL + api_url.format(self.id)
        elif target == 'piece':
            url = BASE_URL + api_url.format(self.id, kwargs["piece"])
        else:
            raise Exception("No such API type")
        return json.loads(requests.get(url).text)

    def get_setts(self):
        self.setts = self.endpoint(API.setts)

    def get_pieces_names(self):
        if self.piece_names is None:
            self.piece_names = self.endpoint(API.piece_names)

    def get_piece_detail(self, piece_id, piece_url):
        return PieceDetails(self, piece_id, piece_url)

    def get_piece_ids(self):
        self.get_pieces_names()

        ids = []
        for p in self.piece_names:
            ids.append(p["id"])

        return ids

    def get_piece_ids_and_urls(self):
        self.get_pieces_names()

        inu = []
        for p in self.piece_names:
            inu.append((p['id'], p['public_url']))

        return inu

    def get_name(self):
        return self.setts['name']

    def get_name_slug(self):
        return self.setts['name_slug']

    def __init__(self, sett_id):
        self.id = sett_id
        self.get_setts()


class PieceDetails:
    json = None
    details = None
    ptr = None

    def follow_ptr(self, ptr_str):
        self.ptr = ptr_str
        return self.json["refs"][ptr_str]

    def get_original_image_url(self):
        suffix = self.details['piece_assets']['image']['original']['url']
        return CLOUDFRONT_PREFIX + suffix

    def get_absolute_url(self):
        return self.details['absolute_url']

    def slug(self):
        a = self.get_absolute_url()
        return a.strip('/').split('/')[-1]

    def __init__(self, sett, piece_id, piece_url):
        self.id = piece_id

        def method_1():
            self.json = sett.endpoint(API.piece_details, target="piece",
                                  piece=self.id)

        def method_2():
            r = requests.get(piece_url, timeout=10.0)
            r.raise_for_status()

            soup = BeautifulSoup(r.text, "lxml")
            res = soup.find(id='piece-detail-piece')
            self.json = json.loads(res['value'])

        def try_methods(l):
            for m in l:
                try:
                    m()
                    if self.json["payload"][0] == "ptr":
                        self.details = self.follow_ptr(self.json["payload"][1])
                    return 0
                except:
                    pass

        global args
        if try_methods([method_1, method_2]) != 0:
            raise
        elif args.verbose:
            print('Found')



class NeonmobUser:
    owned_json = None

    def endpoint(self, api_url, target='user'):
        if target == 'user':
            url = api_url.format(self.id)
        else:
            raise Exception("No such API type")
        return json.loads(requests.get(url).text)

    def setts(self):
        if self.owned_json is None:
            self.owned_json = self.endpoint(API.owned_setts)

        i = 0
        ids = []
        for e in self.owned_json:
            ids.append(e['id'])
            i += 1

        return ids

    def __init__(self, sett_id):
        self.id = sett_id


def get_sett_id(url):
    if "/series/" in url:
        r = requests.get(url, timeout=10.0)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "lxml")
        res = soup.find(string=re.compile("artModule"))


        if res is None:
            # Might be replaced by r.raise_for_status()
            if soup.find(src=re.compile("/static_pages/503\.html")):
                raise Exception("HTTP error code 503 (possible maintenance)")
            else:
                pass

        stm = next(filter(lambda x: "artConfig" in x, str(res).split(";")))
        keyval = next(filter(lambda x: "settId" in x, stm.splitlines()))
        sett_id = int(keyval.split(":")[1].strip(" ,"))

        return sett_id


def get_user_id(url):
    r = requests.get(url, timeout=10.0)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")
    res = soup.find(string=re.compile("artModule"))

    stm = next(filter(lambda x: "artConfig" in x, str(res).split(";")))
    keyval = next(filter(lambda x: "targetId" in x, stm.splitlines()))
    user_id = int(keyval.split(":")[1].strip(" ,"))

    return user_id

def get_username(url):
    l = url.split ('/')

    for i, s in enumerate(l):
        if 'neonmob' in s:
            return l[i+1]


def download_images(sett_id):
    global args
    sett = NeonmobSett(sett_id)

    slug = sett.get_name_slug()
    try:
        os.mkdir(slug)
    except FileExistsError:
        if not args.force:
            raise
    dirname = slug + '/'
    print('Downloading to ' + dirname + '... ', end='')
    if args.verbose: print()

    for id, url in sett.get_piece_ids_and_urls():
        if args.verbose: print('Looking for a JSON for piece', id,
                               'or', url + '... ', end='')
        d = sett.get_piece_detail(id, url)
        img_url = d.get_original_image_url()

        if args.link_only:
            print(img_url)
        else:
            filename = dirname + d.slug()
            with open(filename, 'wb') as f:
                r = requests.get(img_url)
                r.raise_for_status()

                f.write(r.content)
    print('Done')

def main():
    global args

    p = argparse.ArgumentParser()
    p.add_argument('url', action='append')
    p.add_argument('-f', '--force', action='store_true')
    p.add_argument('-v', '--verbose', action='store_true')
    p.add_argument('--link-only', action='store_true',
                   help="List links instead of downloading")
    args = p.parse_args()

    print(args)

    for u in args.url:
        if "series" in u:
            download_images(get_sett_id(u))
        else:
            username = get_username(u)
            print('Downloading all collected setts by ' + username + '...')
            setts = NeonmobUser(get_user_id(u)).setts()
            if args.verbose: print('Found', len(setts), 'setts')
            for id in setts:
                download_images(id)
            print('Done with ' + username)

    return 0


if __name__ == "__main__":
    args = None
    main()
