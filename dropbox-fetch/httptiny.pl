#!/usr/bin/perl

use strict;
use warnings;
use utf8;

use HTTP::Tiny;

my $homepage = shift;
if (not defined $homepage) {die "No homepage given.";}

my $dir = shift;

my $time = time;
my $output = "${dir}filelist/filelist_$time.txt";

open(my $filelist, ">:encoding(utf8)", $output) or die "Can not open file for write : $!";
rec_ls($filelist, "/", $homepage);

# Pipe the output for shell
print $time;


# Fetches the $url and recursively writes to $filelist using $base as the last directory
sub rec_ls {
    my $filelist = shift;
    my $base = shift;
    my $url = shift;
    
    my $client = HTTP::Tiny->new;
    my $response = $client->get($url);
    
    {
    open(my $fh, ">:encoding(utf8)", "response.html") or die "Could not open file for write : $!";
    print $fh $response->{content};
    close $fh;
    }
    
    open my $fh, "<:encoding(utf8)", "response.html" or die "Could not read file : $!";
    
    my $files;
    my $dirs;

    while (<$fh>) { if ( /mod\.initialize_module.*"contents"[:\s]*\{"files"[:\s]*\[([^\[\]]*)\][,\s]*"folders"[:\s]*\[([^\[\]]*)\]/ ) {

        $files = $1;
        $dirs = $2;

    } }

    close $fh;

    if ($files or $dirs) {

        while ($files =~ /"filename"[:\s]*"([^"]*)"/g ) {

            print $filelist "$base$1\n"; 

        }
        
        while ($dirs =~ /"href"[:\s]*"([^"]*)"[^\}]*"filename"[:\s]*"([^"]*)"/g) {

            rec_ls($filelist, "$base$2/", $1);

        }

    } else {
        print $filelist "$base\n"; 
    }


}
