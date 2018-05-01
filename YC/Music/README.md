#1차 한곡으로 만든결과 10곡입니다.

샘플파일 뽑아보기
melody_rnn_generate \
--config=attention_rnn \
--run_dir=/tmp/melody_rnn/logdir/run1 \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--primer_melody="[60]"

학습시키기
melody_rnn_train \
--config=attention_rnn \
--run_dir=/tmp/melody_rnn/logdir/run1 \
--sequence_example_file=/tmp/melody_rnn/sequence_examples/eval_melodies.tfrecord \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--num_training_steps=20000 \
--eval


새로운 멜로디 뽑는 코드
melody_rnn_generate \
--config=attention_rnn \
--run_dir=/tmp/melody_rnn/logdir/run1 \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--primer_melody="[60]"


저장하는 방법
melody_rnn_generate \
--config=attention_rnn \
--run_dir=/tmp/melody_rnn/logdir/run1 \
--hparams="batch_size=64, rnn_layer_sizes=[64,64]" \
--bundle_file=/tmp/attention_rnn.mag \
--save_generator_bundle
