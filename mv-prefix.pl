#!/usr/bin/perl

use strict;
use warnings;

use Cwd;
use File::Copy;

if (@ARGV < 1) {
	die "Missing prefix as argument!\n";
}

my ($target) = @ARGV;

opendir my($dh), getcwd or die "Couldn't open pwd\n$!";
my @files = readdir $dh;
close $dh;

for (@files) {
	if (-f) {
		if ($_ =~ qr/$target(.*)/) {
			move $_, $target . '/' . $1;
		}
	}
}

