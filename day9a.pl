#!/usr/bin/perl

use strict;
use warnings;
use diagnostics;

use feature 'say';
use feature 'switch';

my $lvl9_file = 'day9.txt';
open my $fh, '<', $lvl9_file or die "Error : $_";

my @lines = ();
while (my $line = <$fh>) {
	chomp $line;
	push @lines, $line;
}
my $lines_length = scalar(@lines)-1;
sub recursion {
	my @lineindex = split(",", $_[0]);
	my $index = 0;
	my $right = "None";
	my $left = "None";
	my $up = "None";
	my $down = "None";
	for my $line (0..$lines_length) {
		my @chars = split("", $lines[$line]);
		my $chars_length = scalar(@chars)-1;
		my $y1 = $lineindex[0]-1;
		my $y2 = $lineindex[0]+1;

		if ($y2 != $lines_length+1) {
			if ($line == $y2) {		
				if ($chars[$lineindex[1]] < $_[1]) {
					#say "$chars[$lineindex[1]] at $line,$lineindex[1] is lower than $_[1]";
					$down = recursion("$y2,$lineindex[1]", $chars[$lineindex[1]]);
				}
			}
		}
		if ($y1 != -1) {
			if ($line == $y1) {	
				if ($chars[$lineindex[1]] < $_[1]) {
					#say "$chars[$lineindex[1]] at $line,$lineindex[1] is lower than $_[1]";
					$up = recursion("$y1,$lineindex[1]", $chars[$lineindex[1]]);
				}
			}
		}
		if ($line == $lineindex[0]) {
			my $x1 = $lineindex[1]-1;
			if ($x1 != -1) {
				if ($chars[$x1] < $_[1]) {
					#say "$chars[$x1] at $line,$x1 is lower than $_[1]";
					$right = recursion("$line,$x1", $chars[$x1]);
				}
			}
				
			my $x2 = $lineindex[1]+1;
			if ($x2 != $chars_length+1) {
				if ($chars[$x2] < $_[1]) {
					#say "$chars[$x2] at $line,$x2 is lower than $_[1]";
					$right = recursion("$line,$x2", $chars[$x2]);
				}
			}
		}
		$index += 1;
	}
	if ($up eq "None" && $down eq "None" && $left eq "None" && $right eq "None") {
		return "$_[0]:$_[1]";
	}
}

my $sum = 0;
my %hashes = ();
for my $line (0..$lines_length) {	
	my @chars = split("",$lines[$line]);
	my $chars_length = scalar(@chars)-1;
	foreach my $char (0..$chars_length) {
			my @output = split(":",recursion("$line,$char", $chars[$char]));
			my $result = $output[1]+1;
			$hashes{$output[0]} = $result;
	}
}

for (keys %hashes) {
	say "$_, $hashes{$_}";
	if ($_ ne "") {
		if ($hashes{$_} != 10) {
			$sum += $hashes{$_};
		}
	}
}
say $sum;
close $fh or die "Error : $_";
