#!/bin/bash


BUNDLE_PATH=/home/ys/anaconda3/lib/python3.6/site-packages/magenta/bazel-bin/magenta/models/drums_rnn/drum_kit_rnn.mag

CONFIG=drum_kit_rnn

bazel-bin/magenta/models/melody_rnn/drums_rnn_generate

drums_rnn_generate --config=${CONFIG} --bundle_file=${BUNDLE_PATH} --output_dir=//tmp/drums_rnn/generated --num_outputs=10 --num_steps=128 --primer_drums="[(36,)]"

