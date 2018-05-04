#!/bin/bash


BUNDLE_PATH=/home/ys/anaconda3/lib/python3.6/site-packages/magenta/magenta/models/performance_rnn/performance.mag 


CONFIG=performance


performance_rnn_generate --config=${CONFIG} --bundle_file=${BUNDLE_PATH} --output_dir=/tmp/performance_rnn/generated --num_outputs=10 --num_steps=3000 --primer_melody="[60,62,64,65,67,69,71,72]"
