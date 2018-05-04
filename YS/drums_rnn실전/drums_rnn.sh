#!/bin/bash


INPUT_DIRECTORY=/home/ys/pop2         
#파일이 있는 디렉토리 

SEQUENCES_TFRECORD=/tmp/notesequences.tfrecord
#아웃풋이 저장되는 경로와 파일명

convert_dir_to_note_sequences \
  --input_dir=$INPUT_DIRECTORY \
  --output_file=$SEQUENCES_TFRECORD \
  --recursive
# 컨버팅



drums_rnn_create_dataset \
--config=drum_kit
--input=/tmp/notesequences.tfrecord \
--output_dir=/tmp/drums_rnn/sequence_examples \
--eval_ratio=0.10
# 데이터 셋을 형성!!! 10 %가 평가 컬렉션에 저장 90 %는 교육 컬렉션에 저장


drums_rnn_train \
--config=drum_kit \
--run_dir=/tmp/drums_rnn/logdir/run1 \
--sequence_example_file=/tmp/drums_rnn/sequence_examples/training_drum_tracks.tfrecord \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]}" \
--num_training_steps=1000
#



drums_rnn_generate \
--config=drum_kit \
--run_dir=/tmp/drums_rnn/logdir/run1 \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--output_dir=/tmp/drums_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--primer_drums="[(36, 42), (), (42,)]"
# 드럼비트 
