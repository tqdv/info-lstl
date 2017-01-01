#!/bin/bash

DIR=$(dirname $0)
DIR="$DIR/"

mkdir -p ${DIR}filelist
mkdir -p ${DIR}diff

source ${DIR}config.bash

TIME=`perl ${DIR}httptiny.pl "$URL" "${DIR}";`

sort "${DIR}filelist/filelist_${TIME}.txt" > "${DIR}sorted_${TIME}.txt"
mv "${DIR}sorted_${TIME}.txt" "${DIR}filelist/filelist_${TIME}.txt"

LAST=`cat ${DIR}lasttime`
if [ "$LAST" != '' ]
then
    diff "${DIR}filelist/filelist_${LAST}.txt" "${DIR}filelist/filelist_${TIME}.txt" > "${DIR}diff/diff_${TIME}.txt"
fi

echo $TIME > "${DIR}lasttime"

DIFF=`cat "${DIR}diff/diff_${TIME}.txt"`

if [ "$DIFF" != '' ]
then
    perl ${DIR}mailchimp.pl "$API" "${DIR}diff/diff_${TIME}.txt" "$SUBJECT"
fi

