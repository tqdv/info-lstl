#!/usr/bin/perl

=pod

Version: 0.2.0

Warning: Only use this as a handy shortcut.

Sample use: mv-prefix.pl 'image_(.*).jpg' 'image_${m}.png'

TODO: Add numbering?

=cut

use strict;
use File::Copy;

if (@ARGV < 2) {
	die "Missing prefix as argument!\n";
}

my ($from, $to) = @ARGV;

for (<*>) {
	if ($_ =~ qr/$from/) {
		my $m = $1;
		my $target = $to =~ s/(\$\{\w+\})/$1/eegr;
		move $_, $target;
	}
}

