use strict;
use warnings;

my $current = <>;
while (defined $current) {
	if ($current =~ /^\*([^:]*)$/) {
		$current =~ s/^\*\s+|\s+$//g;
		print "$current % -\n";
		$current = <>;
	} elsif ($current =~ /^\*\s*([^:]*):(.*)$/) {
		my $fst = $1;
		my $snd = $2;

		if ((my $next = <>) =~ /^\*/) {
			print "$fst\%$snd\n";
			$current = <>;
		} else {
			$snd =~ s/"/''/g;
			print "$fst\% \"$snd\n";
			chomp $next;
			print $next;
			while (($next = <>) !~ /^\*/) {
				$next =~ s/"/''/g;
				chomp $next;
				print "\n", $next;
			}
			print "\"\n";
			$current = $next;
		}
	} else {
		$current = <>;
	}
}
