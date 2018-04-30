#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import soundfile as sf

def trans(sound):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/hbk/data/speech_key.json'
    client = speech.SpeechClient()
    file_name = '/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/'+sound
    
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


def soundJar(word):
    dic = {}
    worda
    
if __name__ == '__main__':
    
    print(trans('1_1_A.wav'))


lst = []
lst.append(trans('test.wav'))
lst

구글 ai 

os.listdir('/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut')
import glob
glob.glob('/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/*.wav')
os.getcwd()

import soundfile as sf
f = sf.SoundFile('/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/1_1_A.wav')
print('samples = {}'.format(len(f)))
print('sample rate = {}'.format(f.samplerate))
print('seconds = {}'.format(len(f) / f.samplerate))
