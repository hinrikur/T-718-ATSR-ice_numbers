#!/usr/bin/env perl

$in_list = $ARGV[0];

open IL, $in_list;

while ($l = <L>)
{
	chomp($l);
	$l =~ s/\.wav//;
	$l =~ s/kk1_//;
	$trans = $l;
	$trans =~ s/\_/ /g;
	$trans =~ s/\+/plus/g;
	$trans =~ s/\-/minus/g;
	$trans =~ s/\x/mult/g;
	$trans =~ s/\÷/div/g;
	$trans =~ s/\=/sam/g;
	print "$l $trans\n";
}

# T-718-ATSR/kaldi/egs/open_project/s5/waves_kk1/kk1_-_0_x_6_8_+_2_4_3_1_7_9_5_÷_=.wav
