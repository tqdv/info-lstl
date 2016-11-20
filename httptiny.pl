#!/usr/bin/perl

use strict;
use warnings;

use HTTP::Tiny;

my $client = HTTP::Tiny->new;
my $response = $client->get('http://bit.ly/MPSI3_16-17');

my $answer = $response->{content};

#open(my $fh, ">:encoding(UTF-8)", "response.html");
#print $fh $response->{content};
#close $fh
my @splitted = split $answer , /\n/;
foreach my $line (@splitted) {
    if( $line =~ m/\(.{100}window\.MODULE_CONFIG.{100}\)/) {
        print $1;
        last;
    } else {
        next;
    }
}
die "variable not found";

