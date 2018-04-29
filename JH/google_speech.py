#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:52:28 2018

@author: janghyeonan
"""
import io
import os
import glob
import time
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from pydub import AudioSegment

#구글 음성인식 함수, 변환된 내용을 리턴해줌
def s_t(fname, hhz):
    #구글인증파일 json위치 넣기
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='/Users/janghyeonan/Downloads/*******.json'
    client = speech.SpeechClient()
    file_name = fname
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=hhz, #hhz는 커스텀 주파수로 입력해준다.
        language_code='ko-KR') #한국어로 변경해준다.
    
    response = client.recognize(config, audio)
    talk = []
    for result in response.results:
        talk.append(result.alternatives[0].transcript)
    return talk

#wav파일 헤르츠 찾는 함수, wav파일을 위치를 넣는다.,  해당 파일 헤르츠를 리턴해준다.
def hz_search(url):
    sound = AudioSegment.from_file(url)
    frames_per_second = sound.frame_rate
    return frames_per_second

#음성파일 위치를 넣어주면 제목과 컬럼별(컬럼속 변환 텍스트도들어가 있음)로 짤라서 리스트형으로 리턴해준다.
def st_change(url): 
    res =[]
    file_list=glob.glob(url+"/*.wav")
    cnt = len(file_list)
    for i in file_list[0:5]:
        start_time = time.time()
        hz = hz_search(i)
        text = s_t(i, hz)
        file = os.path.basename(i).split('.')[0]
        b = file.split('_')
        
        if text == []:
            print('['+str(cnt)+']남음 '+os.path.basename(i)+'('+str(hz)+'Hz)', '-> = 경고! 음성인식 내용이 없습니다. =')
            total = file +','+b[0]+','+b[1]+','+b[2]+', '
        else:
            print('['+str(cnt)+']남음 '+os.path.basename(i)+'('+str(hz)+'Hz)', '->', text[0])
            total = file+','+b[0]+','+b[1]+','+b[2]+','+text[0]
        res.append(total)
        
        tt = str((time.time() - start_time) * cnt).split('.')[0]
        if cnt % 10 ==0:
            if int(tt) >= 60:
                print('========= 남은 시간 :'+str(int(tt)/60).split('.')[0]+'분'+str(int(tt)/60).split('.')[1][0:1]+'초 =========')
            else:
                print('========= 남은 시간 :'+tt+'초 =========')
                
        cnt -= 1
    return res
        
if __name__=='__main__':
    st_change('/Users/janghyeonan/it_project2/wav') # 음악 파일 경로를 적어준다.