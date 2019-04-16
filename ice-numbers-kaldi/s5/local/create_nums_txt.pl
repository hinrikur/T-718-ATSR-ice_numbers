#!/usr/bin/env perl

$in_list = $ARGV[0];

open IL, $in_list;

while ($l = <IL>)
{
	chomp($l);
	$l =~ s/\.wav//;
	# $l =~ s/kk1_//g;
	# $l =~ s/kk2_//g;
	# $l =~ s/kv1_//g;
	$trans = $l;
	$trans =~ s/kk1_//g;
	$trans =~ s/kk2_//g;
	$trans =~ s/kv1_//g;
	$trans =~ s/(?<!(kk|kv))1/einn/g;
	$trans =~ s/(?<!(kk|kv))2/tveir/g;
	$trans =~ s/(?<!(kk|kv))3/thrir/g;
	$trans =~ s/(?<!(kk|kv))4/fjorir/g;
	$trans =~ s/5/fimm/g;
	$trans =~ s/6/sex/g;
	$trans =~ s/7/sjo/g;
	$trans =~ s/8/atta/g;
	$trans =~ s/9/niu/g;
	$trans =~ s/0/null/g;
	$trans =~ s/\_/ /g;
	$trans =~ s/\+/plus/g;
	$trans =~ s/\-/minus/g;
	$trans =~ s/(?<=\b)x/mult/g;
	$trans =~ s/\÷/div/g;
	$trans =~ s/\=/sam/g;
	print "$l $trans\n";
}

# T-718-ATSR/kaldi/egs/open_project/s5/waves_kk1/kk1_-_0_x_6_8_+_2_4_3_1_7_9_5_÷_=.wav
