#!/usr/bin/perl

use strict;
use warnings;

# Better way to do it ? (non-experimental)
foreach my $i (@ARGV) {
    ($i eq '--help') && exit print_help();
}

my ($afile, $bfile) = @ARGV;

# Read both input streams

(not defined $afile) && ($afile = '-');
(not defined $bfile) && ($bfile = '-');

my (@alist, @blist);

read_in($afile, \@alist, 1);
read_in($bfile, \@blist, 2);

(!@alist || !@blist) && die "One of the inputs is empty";

# Sort them according to content
@alist = sort { $a->[0] cmp $b->[0] } @alist;
@blist = sort { $a->[0] cmp $b->[0] } @blist;

# Merge the two lists

# @clist = ( [$content, $newrank, $change), ...)
my @clist;
my ($amax, $bmax) = ($#alist, $#blist); # Last elements' index
my ($ai, $bi) = (0, 0);
my $change;

while ($ai <= $amax && $bi <= $bmax) {
    if ($alist[$ai][0] eq $blist[$bi][0]) {
        $change = - ($blist[$bi][1] - $alist[$ai][1]); # Because, sign
        $change = ($change > 0) ? "+$change" : "$change"; # Convert to string
        
        push @clist, [$alist[$ai][0], $blist[$bi][1], $change];
        $ai++; $bi++;
    } elsif ($blist[$bi][0] lt $alist[$ai][0]) {
        push @clist, [$blist[$bi][0], $blist[$bi][1], '+'];
        $bi++;
    } elsif ($alist[$ai][0] lt $blist[$bi][0]) {
        push @clist, [$alist[$ai][0], $alist[$ai][1], '-'];
        $ai++;
    } else {
        die "String comparison somehow failed\n"
    }

}

# Now add all the elements left if any
add_remaining($ai, $amax, \@alist, \@clist, '-');
add_remaining($bi, $bmax, \@blist, \@clist, '+');

# Sort according to $bfile's rank
@clist = sort { $a->[1] <=> $b->[1] } @clist;

foreach my $elem (@clist) {
    print "$$elem[1] $$elem[2] $$elem[0]\n";
}
sub print_help {
    print "Usage: $0 FILE1 FILE2\n";
    print "If FILE1 or FILE2 is -, read STDIN\n";
}

sub fill_arr {
    my ($arrref, $line, $lnref) = @_;

    $$lnref++;
    chomp $line;
    push @$arrref, [$line, $$lnref];
}

sub read_in {
    my ($filename, $arrayref, $filenum) = @_;

    my $ln = 0; # Number of lines processed
    
    if ($filename eq '-') {
        while (<STDIN>) {
            fill_arr($arrayref, $_, \$ln);
        }
        print "Read FILE$filenum\n";
    } else {
        open(my $fh, '<', $filename) or die "Can't open $filename: $!";
        while(<$fh>) {
            fill_arr($arrayref, $_, \$ln);
        }
        close($fh) or warn "Closing $filename failed: $!";
    }
}

sub add_remaining {
    my ($start, $end, $origin, $destination, $sign) = @_;

    if ($start <= $end) {
        for my $i ($start..$end) {
            push @$destination, [$$origin[$i][0], $$origin[$i][1], $sign];
        }
    }
}
