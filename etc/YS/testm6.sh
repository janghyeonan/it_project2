#!/bin/bash

BUNDLE_PATH=/home/ys/anaconda3/lib/python3.6/site-packages/magenta/magenta/models/polyphony_rnn/polyphony_rnn.mag


polyphony_rnn_generate  --bundle_file=${BUNDLE_PATH}  -output_dir=/tmp/polyphony_rnn/generated --num_outputs=10 --num_steps=128 --primer_pitches="[67,64,60]" --condition_on_primer=true --inject_primer_during_generation=false

