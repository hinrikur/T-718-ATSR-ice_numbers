#!/bin/bash

train_cmd="utils/run.pl"
decode_cmd="utils/run.pl"

train_nums=train_nums
test_base_name=test_nums

rm -rf data exp mfcc

# Data preparation

local/prepare_data.sh waves_nums
local/prepare_dict.sh
utils/prepare_lang.sh --position-dependent-phones false data/local/dict "<SIL>" data/local/lang data/lang
local/prepare_lm.sh

# Feature extraction
for x in train_nums test_nums; do
 utils/fix_data_dir.sh data/$x/utt2spk
 steps/make_mfcc.sh --nj 1 data/$x exp/make_mfcc/$x mfcc
 steps/compute_cmvn_stats.sh data/$x exp/make_mfcc/$x mfcc
 utils/fix_data_dir.sh data/$x
done

# Mono training
steps/train_mono.sh --nj 1 --cmd "$train_cmd" \
  --totgauss 400 \
  data/train_nums data/lang exp/mono0a

# Graph compilation
utils/mkgraph.sh data/lang_test_tg exp/mono0a exp/mono0a/graph_tgpr

# Decoding
steps/decode.sh --nj 1 --cmd "$decode_cmd" \
    exp/mono0a/graph_tgpr data/test_nums exp/mono0a/decode_test_nums

for x in exp/*/decode*; do [ -d $x ] && grep WER $x/wer_* | utils/best_wer.sh; done
