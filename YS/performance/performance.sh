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



CONFIG=performance_with_dynamics
performance_rnn_create_dataset \
--config=${CONFIG} \
--input=/tmp/notesequences.tfrecord \
--output_dir=/tmp/performance_rnn/sequence_examples \
--eval_ratio=0.10
# 데이터 셋을 형성 



performance_rnn_train \
--config=${CONFIG} \
--run_dir=/tmp/performance_rnn/logdir/run1 \
--sequence_example_file=/tmp/performance_rnn/sequence_examples/training_performances.tfrecord
# 트레이닝을 한다 



performance_rnn_generate \
--run_dir=/tmp/performance_rnn/logdir/run1 \
--output_dir=/tmp/performance_rnn/generated \
--config=${CONFIG} \
--num_outputs=10 \
--num_steps=3000 \
--primer_melody="[60,62,64,65,67,69,71,72]"
# 멜로디를 생성하여 mid파일로 저장 

