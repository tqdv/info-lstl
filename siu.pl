#!/usr/bin/perl

# Dropped

use strict;
use warnings;

# Debug levels
my $d = 0;
my $dd = 0;
my $inputfile;

($inputfile, $d, $dd) = @ARGV;

open my $fh, '<', $inputfile or die "Could not open $inputfile : $!";

my %unittree;

{
my $line;
if (not defined($line = <$fh>)) { die "No input"; }
my @baseunits = split ' ', $line; # splitting on ' ' <=> on /\s+/

if ($d) {
print "DEBUG baseunits: @baseunits\n";
($dd) && <STDIN>;
}

# Add baseunits to unittree
foreach my $unit (@baseunits) {
	$unittree{$unit."1"} = {
		value => {
			$unit => 1
		},
		above => [],
		level => 1
	}
}

# Add 1 to unittree
@baseunits = map {$_ . "1"} @baseunits;  # Convert to unit1
$unittree{"1"} = {
	value => {},
	above => [ @baseunits ],
	level => 0
};

if ($d) {
print "DEBUG Added baseunits\n";
($dd) && <STDIN>;
print_ut();
($dd) && <STDIN>;
}

}

while (defined(my $line = <$fh>)) {
	my ($unitsymb, $unitexpr) = (split ' ', $line);
	
	# Create the value hash for the current unit
	my %unitval;
	while ($unitexpr =~ m!([a-zA-Z]+)(-?[0-9]*)!g) {
		if (not exists $unitval{"$1"}) {
			$unitval{"$1"} = ($2 ne "" ? (int $2) : 1);
		} else {
			$unitval{"$1_alt"} = $2;
		}
	}

	if ($d) {
	print "Adding $unitsymb:\n";
	foreach my $key (keys %unitval) {
		print "\t$key: $unitval{$key}\n";
	}
	($dd) && <STDIN>;
	}

	# Create non-existent baseunits powers
	foreach my $elem (keys %unitval) {
		add_baseunit($elem, $unitval{"$elem"});
	}

	# Calculate level
	my $level; 
	map { $level += $_ } (values %unitval);

	# Add unit to unittree
	$unittree{"$unitsymb"} = {
			value => \%unitval,
			above => [],
			level => $level
	};
	
	if ($d) {
	print "DEBUG Added $unitsymb:\n";
	my @keys = keys %unitval; 
	print "\t@keys\n";
	print "\tlevel: $level\n";
	($dd) && <STDIN>;
	}

	# Fill the aboves
	# Go through tree starting from each base component
	my $seen = {};
	foreach my $elem (keys %unitval) {
		if ($d) {
		print "Adding $unitsymb from $elem\n";
		($dd) && <STDIN>;
		}
		add_from($elem . $unitval{$elem}, \%unitval, $unitsymb, $seen);
		if ($d) {
		print "Added $unitsymb from $elem\n";
		print_ut();
		($dd) && <STDIN>;
		}
	}
}
close $fh;

if ($d) {
print "FINAL PRINT!!!!!!\n";
print "-----------------\n";
print "-----------------\n";
print "-----------------\n";
($dd) && <STDIN>;
print_ut();
}

# Writing output
# Removing _alt and replacing - with _neg_ because graphviz
# doesn't like it
open $fh, '>', "file.gv";
print $fh "digraph G {\n";
foreach my $key (keys %unittree) {
	# $n* is used for printing, $* is the internal representation
	my $nkey = ($key =~ s/-/_neg_/r);
	if ($nkey =~ m/_alt/) {
		# Compare with the alternate version to prevent duplicates
		my $ori = ($key =~ s/_alt//r);
		$nkey =~ s/_alt//;

		# %seen holds the internal representations
		my %seen;
		map { my $e = (s/_alt//r); $seen{$e} = 1 } @{ $unittree{$ori}->{above} };

		foreach my $elem (@{ $unittree{$key}->{above} }) {
			my $nelem = ($elem =~ s/_alt//r);
			if (not exists $seen{$nelem}) {
				$seen{$nelem} = 1;
				$nelem = ($nelem =~ s/-/_neg_/r);
				print $fh "$nkey -> $nelem;\n";
			}
		}

	} else {
		# %seen holds the external representation
		my %seen;
		foreach my $elem (@{ $unittree{$key}->{above} }) {
			my $nelem = (($elem =~ s/-/_neg_/r )=~ s/_alt//r);
			if (not exists $seen{$nelem}) {
				$seen{$nelem} = 1;
				print $fh "$nkey -> $nelem;\n";
			}
		}
	}
}
print $fh "}";

close $fh;

sub print_ut {
	foreach my $key (keys %unittree) {
		print "unit: $key\n";
		print "\tvalue:\n";
		{
		my %valueh = %{ $unittree{$key}->{'value'} }; # value hash
		foreach my $unitkey (keys %valueh) {
			print "\t\t$unitkey: $valueh{$unitkey}\n";
		}
		}
		print "\tabove:\n";
		foreach my $elem (@{ $unittree{$key}->{'above'} }) {
			print "\t\t- $elem\n";
		}
		print "\tlevel: $unittree{$key}->{'level'}\n";
	}
}

sub print_u {
	my ($unit) = @_;

	print "$unit:\n";
	print "\tvalue:\n";
	foreach my $bunit (keys %{ $unittree{$unit}->{'value'} }) {
		print "\t\t$bunit: $unittree{$unit}->{'value'}{$bunit}\n";
	}
	print "\tabove: @{ $unittree{$unit}->{'above'} }\n";
	print "\tlevel: $unittree{$unit}->{'level'}\n";
}

sub cmp_vals {
# Returns -1, 0, 1 if leftside is less than, equal, or greater than rightside
# Or 63 if it is undecidable
	my ($ahashref, $bhashref) = @_;

	my @akeys = sort keys %$ahashref;
	my @bkeys = sort keys %$bhashref;
	my @cmps;

	# Fill @cmps with key <=> key
	while (@akeys || @bkeys) {
		if (@akeys && @bkeys && $akeys[0] eq $bkeys[0]) {
			my $akey = shift @akeys;
			my $bkey = shift @bkeys;

			push @cmps, $ahashref->{$akey} <=> $bhashref->{$bkey};

		} elsif (@akeys && @bkeys && $akeys[0] lt $bkeys[0]
		         or @akeys && ! @bkeys) {
			my $akey = shift @akeys;
			my $aval = $ahashref->{$akey};

			if ($aval != 0) {
				push @cmps, 1;
			} else { warn "Added a zero to value"; }

		} elsif (@akeys && @bkeys && $akeys[0] gt $bkeys[0]
		         or ! @akeys && @bkeys) {
			my $bkey = shift @bkeys;
			my $bval = $bhashref->{$bkey};

			if ($bval != 0) {
				push @cmps, -1;
			} else { warn "Added a zero to value"; }
		}
	}

	if (! @cmps) { warn "No comparison done\n"; return; }

	my $first = shift @cmps;
	foreach my $elem (@cmps) {
		if ($elem == 0 || $elem == $first) {
			next;
		}
		if ($first == 0) {
			$first = $elem;
			next;
		}
		# case $first != $elem and $first != 0 and $elem != 0
		return 63; # '?' in Unicode
	}
	return $first;
}

sub add_baseunit {
	my ($unit, $expon) = @_;

	$expon == 0 && return; # 1 is already added
	if (exists $unittree{$unit . $expon}) { return; }
	
	if ($d) {
	print "DEBUG Added from $unit$expon...\n";
	($dd) && <STDIN>;
	}
	
	my $oriexpon = $expon;
	my $sign = ($expon > 0 ? "+" : "-");

	my $extrunit = $unit . $expon; # Key in unittree (extracted unit)
	while ($expon != 0 && ! exists($unittree{$extrunit})) {
		my $above = ($expon == -1 ? 1 : $unit . ($expon +1));
		
		$unittree{$extrunit} = {
			value => {
				$unit => int $expon
			},
			above => [ $above ],
			level => int $expon
		};

		if ($d) {
		print_u($extrunit);
		($dd) && <STDIN>;
		}

		$expon = $expon - (int "${sign}1");
		$extrunit = ( $expon == 0 ? 1 : $unit . $expon);
		if ($d) {
		print "Trying to add $extrunit\n";
		($dd) && <STDIN>;
		}
	}

	if ($d) {
	print "...to $unit$expon\n";
	($dd) && <STDIN>;
	}

	# Positive decreasing, add above for the last one
	if ($oriexpon > 0 ) {
		if ($d) {
		print "extrunit: $extrunit\n";
		print "expon: $expon\n";
		($dd) && <STDIN>;
		}
		push @{ $unittree{$extrunit}->{'above'} }, $unit . ($expon +1);
		pop @{ $unittree{$unit . $oriexpon}->{'above'} };
	}

	if ($d) {
	foreach my $i (($expon + 1)..$oriexpon) {
		print_u($unit . $i);
	}
	($dd) && <STDIN>;
	}
}

sub add_from {
	my ($from, $unitval, $unitsymb, $seen) = @_;
	
	if ($from eq $unitsymb) { return; }

	if (exists $seen->{$from}) { return; }
	$seen->{$from} = 1;

	my $comparison = cmp_vals($unitval, $unittree{$from}->{'value'});
	if ($d) {
	print "DEBUG comparison: $unitsymb $comparison $from\n";
	print_u($unitsymb);
	print_u($from);
	($dd) && <STDIN>;
	}

	if ($comparison == 0) {
		push @{ $unittree{$from}->{'above'} }, $unitsymb;
		push @{ $unittree{$unitsymb}->{'above'} }, $from;

	} elsif ($comparison == -1) {
		warn "Error, checking against greater unit";

	} elsif ($comparison == 1) {
		my $isabove = 0;
		my @fabove; # The new above for $from
		my @uabove; # The new above for $unitsymb

		if ($d) {
		print "DEBUG going through @{ $unittree{$from}->{'above'} }\n";
		($dd) && <STDIN>;
		}

		foreach my $elem (@{ $unittree{$from}->{'above'} }) {
			my $upcomp = cmp_vals($unitval, $unittree{$elem}->{'value'});

			if ($elem eq '1') { # Otherwise it just goes up
				push @fabove, "1";
				next;
			}
			if ($upcomp == 1 || $upcomp == 0) {
				$isabove = 1;
				push @fabove, $elem;
				add_from($elem, $unitval, $unitsymb, $seen);
			}
			if ($upcomp == -1) {
				if (not exists $seen->{$upcomp}) {
					$seen->{$upcomp} = 1;
					push @uabove, $elem;
				}
			}
			if ($upcomp == 63) {
				push @fabove, $elem;
			}
		}

		(! $isabove) && (push @fabove, $unitsymb);

		# Replacing into the tree
		$unittree{$from}->{above} = \@fabove;
		push @uabove, @{ $unittree{$unitsymb}->{above} }; 
		$unittree{$unitsymb}->{above} = \@uabove;

		if ($d) {
		print "fabove: @fabove\n";
		print "uabove: @uabove\n";
		($dd) && <STDIN>;
		}
	}
}

sub check_alt {
	my ($name, $var) = @_;

	if ($name =~ /_alt/) {
		return  - $var;
	}
	return $var;
}

sub uniq {
	my %seen;
	grep !$seen{$_}++, @_;
}
