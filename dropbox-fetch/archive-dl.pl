#!/usr/bin/perl

use strict;
use warnings;

use HTTP::Tiny;

my ($url, $location) = @ARGV;

if (not defined $url) { die "No homepage given"; }
# if (not defined $location) { die "No file location given"; }

my $client = HTTP::Tiny->new;
my $response = $client->get($url);
my $content = $response->{content};

open my $fh, "<", \$content;

my $ar_url;
while (<$fh>) {
	# Thing that you'll have to change often because of code updates
	if (/InitReact.*?"folderSharedLinkInfo".*?\{.*?"url".*?"([^"]*)"/) {
		print $1;
		$ar_url = $1 . '?dl=1';
		last;
	}
}

close $fh;
open my $out, ">", 'out.html';

$response = $client->get($ar_url);
$content = $response->{content};
print $out $content;
close $out;
