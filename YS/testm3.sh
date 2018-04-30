#!/bin/bash


BUNDLE_PATH=/home/ys/anaconda3/lib/python3.6/site-packages/magenta/bazel-bin/magenta/models/improv_rnn/chord_pitches_improv.mag


CONFIG=chord_pitches_improve


improv_rnn_generate --config=${CONFIG} --bundle_file=${BUNDLE_PATH} --output_dir=/tmp/improv_rnn/generated --num_outputs=10 --primer_melody="[60]" --backing_chords="C G Am F C G Am F" --render_chords
