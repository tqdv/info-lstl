#!/usr/bin/perl

use strict;
use warnings;

use HTTP::Tiny;

{
$filelist = shift;
$base = shift;
$url = shift;

#my $client = HTTP::Tiny->new;
#my $response = $client->get('http://bit.ly/MPSI3_16-17');
#
#{
#open(my $fh, ">:encoding(UTF-8)", "response.html");
#print $fh $response->{content};
#close $fh
#}

open my $fh, "<", "response.html" or die $!;

my $content;

while ( ($content = <$fh>) !~ /mod\.initialize_module/ ) { }

if (defined $content) {

    if ($content =~ /"contents": \{"files": \[([^\]]*)\], "folders": \[([^\]]*)\]/ ) {
        print "Here are the files :\n", $1, "\nHere are the folders :\n", $2, "\n";
        
        if ($1 ne '') {
        # Do stuff here
        } 
        
        if ($2 ne '') {
            

    } else { print "Incorrect syntax, check regexp\n" }

} else {print "No match found"} 

}
