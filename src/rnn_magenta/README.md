# 마젠타 관련 설명

## 각 항목별 설명
### Data File : 데이터셋 모으는 방법(크롤링을 통해서 Midi파일 수집)

crawling.py : 크롤링 방법 \
  ※ 크롤링시 파일 다운로드 경로와 추후 마젠타 가동시에 사용할 input경로를 동일하게 지정해 주어야 한다.

### Magenta_step File : 준비된 데이터셋(Midi file)과 셋팅된  마젠타를 가지고 음악파일(Midi file)을 생성하는 방법
#### 경로 설정 

$ INPUT_DIRECTORY=/home/itwill02/바탕화면/it/rnb       # 학습시킬 노래 넣어둔 파일 \
$ SEQUENCES_TFRECORD=/tmp/notesequences.tfrecord    # tfrecord파일 생성할 곳 

tfrecord_create.txt : tfrecord 파일 생성 코드

train_test_divide.txt : 학습,테스트 나누는 코드

train.txt : 학습시키는 코드

create.txt : 새로운 멜로디 뽑는 코드

### Result file : 결과물 들어보기
midi 파일 재생시켜 보기 \

$ sudo apt install timidity # timidity라는 패키지 이용 \ 
$ timidity {PATH} # PATH는 생성한 Midi파일의 경로를 지정해 준다.




### 결과물 통합과정 거쳐야 할듯함.
