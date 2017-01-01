#!/usr/bin/perl

use warnings;
use strict;

my $api = shift;
my $file = shift;
my $subject = shift;
my $serv;
my $list;
my $answer;
my $campaign;
my $content = `cat $file`;

if($api =~ /-(.*)/) {
    $serv = $1;
}

$answer = `curl --silent --request GET --url 'https://${serv}.api.mailchimp.com/3.0/lists' --user 'anystring:${api}'`;

if($answer =~ /"id"[:\s]*"([^"]*)"[^"]*"name"[:\s]*"MPSI 3"/s) {
    $list = $1;
}

$answer = `curl --silent --request POST --url 'https://${serv}.api.mailchimp.com/3.0/campaigns' --user 'anystring:${api}' --data '{"recipients": {"list_id": "${list}"}, "type": "regular", "settings": {"subject_line": "${subject}", "from_name": "SimplyCurious", "reply_to": "tiwa.qendov\@gmail.com"}}'`;

if($answer =~ /"id"[:\s]*"([^"]*)"/) {
    $campaign = $1;
}

`curl --silent --request PUT --url 'https://${serv}.api.mailchimp.com/3.0/campaigns/${campaign}/content' --user 'anystring:${api}' --data '{"html": "<pre>${content}</pre>"}'`;

`curl --silent --request POST --url 'https://${serv}.api.mailchimp.com/3.0/campaigns/${campaign}/actions/send' --user 'anystring:${api}'`;

