#!/usr/bin/env perl

$waves_dir = $ARGV[0];
$in_list = $ARGV[1];

open IL, $in_list;

while ($l = <IL>)
{
	chomp($l);
	$full_path = $waves_dir . "\/" . $l;
	$l =~ s/\.wav//;
	# $l =~ s/x/\*/;
	# $l =~ s/kk1_//;
	# $l =~ s/kk2_//;
	# $l =~ s/kv1_//;
	# $l =~ s/1/einn/g;
	# $l =~ s/2/tveir/g;
	# $l =~ s/3/thrir/g;
	# $l =~ s/4/fjorir/g;
	# $l =~ s/5/fimm/g;
	# $l =~ s/6/sex/g;
	# $l =~ s/7/sjo/g;
	# $l =~ s/8/atta/g;
	# $l =~ s/9/niu/g;
	# $l =~ s/0/null/g;
	# $l =~ s/\+/plus/g;
	# $l =~ s/\-/minus/g;
	# $l =~ s/(?<=\b)x/mult/g;
	# $l =~ s/(?<=\_)x/mult/g;
	# $l =~ s/\÷/div/g;
	# $l =~ s/\=/sam/g;
	print "$l $full_path\n";
}
