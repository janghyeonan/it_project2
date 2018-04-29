★ 머신/딥러닝 프로젝트 2 (김태효) ★
===================
## [1] 진행하는 주제
 - 억양에 따른 감정분석

## [2] 부여된 업무
 - b3. 모델 찾아서 우선은 텍스트로 뽑아내기
 - b4. 높낮이를 구분하여 감정(레벨에 따른) 구별해 내기

## [3] 폴더구성 및 설명

 - 참고코드 : 구글 스피치 API를 파이썬 코드로 공개한 자료(원본, 압축본) 게시하였음 (출처 : 참고자료 3)
 - stt.py : 실시간 음성을 텍스트로 변환해서 보여주는 프로그램
 - trans.py : 음서파일을 텍스트로 변환해서 보여주는 프로그램(다수의 파일을 텍스트로 변환해서 데이터프레임에 넣을 수 있도록 수정중)
 - emotion.py : 음성파일을 통해 감정분석하는 프로그램(librosa 사용 : 참고자료 8)

## [4] 참고자료

#### 1. 구글 AI, Voice 등 딥러닝 연구
 - https://experiments.withgoogle.com/

#### 2. 언어분석
 - http://bnr.co.kr/service/scientific-language/

#### 3. 구글 API code 및 각종 보물창고
 - http://blog.naver.com/PostList.nhn?blogId=chandong83

#### 4. 최근우 박사 블로그(논문풀이)
 - http://keunwoochoi.blogspot.kr/?m=1

#### 5. 음성 -> 텍스트 변환하는 예제
 - https://webrtclab.herokuapp.com/speech-recognition/
 - (코드) https://github.com/dodortus/webrtc-lab/blob/master/views/examples/speech-recognition/main.js?ts=2
 - https://github.com/jybaek/gcp_speech_api/

#### 6. 구글 클라우드 깃허브에 게시된 파이썬 코드 
 - https://github.com/GoogleCloudPlatform/python-docs-samples
 
#### 7. soundfile 모듈(오디오 파일의 세부정보 추출시 사용, ex.샘플률 16000,48000 등)
 - https://github.com/bastibe/SoundFile

#### 8. librosa 사용방법(감정분석시에 사용할 패키지)
 - https://librosa.github.io/
 
