#!/usr/bin/env perl
import sys

full_list = sys.argv[1]
test_list = sys.argv[2]
train_list = sys.argv[3]

FL = [
	'kk1_+_6_÷_=_5_9_4_2_3_1_0_-_x_8_7.wav',
	'kk1_+_8_x_0_4_2_3_-_1_9_÷_5_=_7_6.wav',
	'kk1_-_0_x_6_8_+_2_4_3_1_7_9_5_÷_=.wav',
	'kk1_-_2_6_=_9_5_8_0_4_x_3_1_+_7_÷.wav',
	'kk1_-_x_4_2_1_÷_0_3_9_7_6_=_8_+_5.wav',
	'kk1_0_4_÷_3_9_-_7_1_8_+_2_6_=_x_5.wav',
	'kk1_1_7_4_9_=_5_+_0_x_8_÷_3_-_2_6.wav',
	'kk1_1_=_+_x_5_4_3_÷_9_2_8_7_-_6_0.wav',
	'kk1_2_9_÷_=_8_7_0_6_1_3_+_x_5_4_-.wav',
	'kk1_4_+_6_2_8_7_0_9_=_-_5_1_x_3_÷.wav',
	'kk1_4_1_x_5_9_÷_8_7_6_+_3_=_0_-_2.wav',
	'kk1_4_6_3_1_7_2_8_+_x_=_÷_0_-_9_5.wav',
	'kk1_5_6_+_1_7_2_-_0_=_9_÷_4_x_8_3.wav',
	'kk1_5_=_6_1_3_2_7_9_8_4_-_÷_0_+_x.wav',
	'kk1_6_1_7_÷_2_+_x_8_-_9_0_=_4_3_5.wav',
	'kk1_6_8_5_-_+_4_1_7_9_=_2_0_x_3_÷.wav',
	'kk1_9_6_x_5_2_1_=_3_8_4_-_÷_7_+_0.wav',
	'kk1_=_÷_5_x_3_1_-_6_8_7_2_9_+_4_0.wav',
	'kk1_x_5_=_-_8_6_+_7_0_4_1_9_2_÷_3.wav',
	'kk1_x_7_-_÷_=_4_8_0_9_1_6_5_2_+_3.wav',
]

'''
with open(full_list 'r') as FL:

	TESTLIST = open(test_list, 'w')
	TRAINLIST = open(train_list, 'w')
'''

nol = 0
i = 0
for line in FL:
	nol += 1




# open FL, $full_list;
# $nol = 0;
# while ($l = <FL>)
# {
# 	$nol++;
# }
# close FL;

# $i = 0;
# # open FL, $full_list;
# open TESTLIST, ">$test_list";
# open TRAINLIST, ">$train_list";
# while ($l = <FL>)
# {
# 	chomp($l);
# 	$i++;
# 	if ($i <= $nol/2 )
# 	{
# 		print TRAINLIST "$l\n";
# 	}
# 	else
# 	{
# 		print TESTLIST "$l\n";
# 	}
# }