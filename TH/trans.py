#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def trans(sori):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/hbk/data/speech_key.json'
    client = speech.SpeechClient()
    file_name = '/Users/hbk/data/python-docs-samples/speech/cloud-client/file/'+sori
    
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ko-KR')
    
    response = client.recognize(config, audio)
    
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        
if __name__ == '__main__':
    trans('test.wav')