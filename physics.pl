#!/bin/env perl

use strict;
use warnings;

# Modules
use Web::Query;

my $count = 0;
my $start;
while($count == 0) {
$Web::Query::UserAgent = LWP::UserAgent->new( agent => 'Lynx/2.8.8dev.3 libwww-FM/2.14 SSL-MM/1.4.1' );

$start = Web::Query->new('http://bit.ly/MPSI3_16-17');
$count = $start->find('a.thumb-link')->size;
}

if ($start->as_html =~ m!<title>(.*)</title>!) { print "Title : $1\n"; } 

$start->find('a')->each(sub {
  my $i = shift;
  print $i.":: ".$_->as_html."\n";
});

if ($start->as_html =~ m!(.{130}Devoirs.{30})! ) { print "yes: $1\n" }
