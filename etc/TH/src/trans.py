#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import soundfile as sf

def trans(path,sound):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/hbk/data/speech_key.json'
    client = speech.SpeechClient()
    file_name = path+sound
    
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sf.SoundFile(file_name).samplerate,
        language_code='ko-KR')
    
    response = client.recognize(config, audio)
    
    for result in response.results:
        #print('Transcript: {}'.format(result.alternatives[0].transcript))
        res = result.alternatives[0].transcript
    return res

def display():
    path = input("폴더경로를 입력하시오 : ")
    sound = input("음성파일을 입력하시오 : ")
    return path,sound


if __name__ == '__main__':
    path, sound = display()
    #path = '/Users/hbk/data/python-docs-samples/speech/cloud-client/file/'
    #sound = 'test.wav'
    print("음성파일 문자로 변환중...")
    res = trans(path,sound)
    print("\n변환결과 :",res)
