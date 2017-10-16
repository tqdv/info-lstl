use strict;
use warnings;

sub trim {
	my ($str) = @_;
	$str =~ s/^\*\s+|\s+$//g;
	return $str;
}

sub escape {
	my ($str) = @_;
	$str =~ s/</&lt;/g;
	$str =~ s/>/&gt;/g;
	return $str;
}


my $current = <>;
while (defined $current) {
	if ($current =~ /^\*([^:]*)$/) {
		$current = escape(trim($current));
		print "$current % -\n";
		$current = <>;
	} elsif ($current =~ /^\*\s*([^:]*):(.*)$/) {
		my $fst = escape(trim($1));
		my $snd = escape(trim($2));

		if ((my $next = <>) =~ /^\*/) {
			# Single line key-value pair
			print "$fst % $snd\n";
			$current = <>;
		} else {
			print "$fst % $snd<br>";
			chomp $next;
			print $next;
			while (($next = <>) !~ /^\*/) {
				chomp $next;
				print "<br>", $next;
			}
			print "\n";
			$current = $next;
		}
	} else {
		$current = <>;
	}
}
