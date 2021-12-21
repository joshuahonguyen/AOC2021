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

my %hashes = ();
for my $line (0..$lines_length) {	
	my @chars = split("",$lines[$line]);
	my $chars_length = scalar(@chars)-1;
	foreach my $char (0..$chars_length) {
			my @output = split(":",recursion("$line,$char", $chars[$char]));
			my $result = $output[1];
			$hashes{$output[0]} = $result;
	}
}
my %flood_hash = ();
my $flood_val = -1;
sub flood {
	my @params = split(",", $_[0]);
	my $l = $params[0];
	my $i = $params[1];

	my @default = split(",", $flood_val);
	my $l_def = $default[0];
	my $i_def = $default[1];
	for my $line (0..$lines_length) {
		my @chars = split("", $lines[$line]);
		my $chars_length = scalar(@chars)-1;

		my $up = $l-1;
		my $down = $l+1;
		my $left = $i-1;
		my $right = $i+1;

		my $a = -1;
		my $b = -1;
		my $c = -1;
		my $d = -1;
		
		if ($line == $l) {
			if ($left > -1 && $left < $i_def) {
				if ($chars[$left] != 9) {	
					$a = $chars[$left];
					$flood_hash{"$line,$left"} = $a;
					flood("$line,$left");
				}
			}	
			if ($right < $chars_length+1 && $right > $i_def) {
				if ($chars[$right] != 9) {
					$b = $chars[$right];
					$flood_hash{"$line,$right"} = $b;
					flood("$line,$right");
				}
			}
		}
		if ($line == $up) {
			if ($up > -1 && $up < $l_def) {
				if ($chars[$i] != 9) {
					$c = $chars[$i];
					$flood_hash{"$up,$i"} = $c;
					flood("$up,$i");
				}
			}
		}
		if ($line == $down) {
			if ($down < $lines_length+1 && $down > $l_def) {
				if ($chars[$i] != 9) {
					$d = $chars[$i];
					$flood_hash{"$down,$i"} = $d;
					flood("$down,$i");
				}
			}
		}
	}
}
my @large_array = ();
my $sum = 0;
for (keys %hashes) {
	if ($_ ne "") {
		if ($hashes{$_} != 9) {
			%flood_hash = ($_ => $hashes{$_});
			$flood_val = $_;
			flood($_);
			my $i_hash = 0;
			for (keys %flood_hash) {
				$i_hash += 1;
			}
			push(@large_array, $i_hash);
		}
	}
}
my @sorted = sort { $a <=> $b } @large_array;
my $largest3 = $sorted[-3];
my $largest2 = $sorted[-2];
my $largest1 = $sorted[-1];
say $largest3;
say $largest2;
say $largest1;
$sum = $largest2 * $largest1 * $largest3;
say $sum;
close $fh or die "Error : $_";
