#!/bin/bash

BUNDLE_PATH=//home/ys/anaconda3/lib/python3.6/site-packages/magenta/magenta/models/melody_rnn/basic_rnn.mag


CONFIG=basic_rnn

bazel-bin/magenta/models/melody_rnn/melody_rnn_generate

melody_rnn_generate --bundle_file=${BUNDLE_PATH} --output_dir=//tmp/generated --num_outputs=10 --num_steps=128 --primer_melody="[60]"
