#1차 한곡으로 만든결과 10곡입니다.


INPUT_DIRECTORY=/home/itwill02/바탕화면/it/rnb    #노래 끌어올곳 \
SEQUENCES_TFRECORD=/home/itwill02/바탕화면/it/notesequences.tfrecord #tfrecord파일 생성할 곳 \

파일 시동걸기 \

convert_dir_to_note_sequences \
--input_dir=$INPUT_DIRECTORY  \
--output_file=$SEQUENCES_TFRECORD  \
--recursive


학습,테스트 나누기 \

melody_rnn_create_dataset \
--config=attention_rnn \
--input=/tmp/notesequences.tfrecord  \
--output_dir=/tmp/melody_rnn/sequence_examples  \
--eval_ratio=0.10





학습시키기 \

melody_rnn_train \
--config=attention_rnn \
--run_dir=/tmp/melody_rnn/logdir/run1 \
--sequence_example_file=/tmp/melody_rnn/sequence_examples/eval_melodies.tfrecord \
--hparams="batch_size=64,rnn_layer_sizes=[64,64],learning_rate = 0.0001" \
--num_training_steps=20000 \
--eval


새로운 멜로디 뽑는 코드 \ 

melody_rnn_generate \
--config=attention_rnn \
--run_dir=/tmp/melody_rnn/logdir/run1 \
--output_dir=/tmp/melody_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--primer_melody="[60]"


저장하는 방법 \

melody_rnn_generate \
--config=attention_rnn \
--run_dir=/tmp/melody_rnn/logdir/run1 \
--hparams="batch_size=64, rnn_layer_sizes=[64,64]" \
--bundle_file=/tmp/attention_rnn.mag \
--save_generator_bundle


midi재생시켜 보기 \ 

sudo apt install timidity \ 
timidity 경로 \ 



그리고 1차학습 결과물
