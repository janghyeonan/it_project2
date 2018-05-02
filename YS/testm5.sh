#!/bin/bash


BUNDLE_PATH=/home/ys/anaconda3/lib/python3.6/site-packages/magenta/magenta/models/pianoroll_rnn_nade/pianoroll_rnn_nade.mag

pianoroll_rnn_nade_generate --bundle_file=${BUNDLE_PATH} --output_dir=/tmp/pianoroll_rnn_nade/generated --num_outputs=10 --num_steps=128 --primer_pitches="[67,64,60]"

