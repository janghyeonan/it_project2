#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 음성파일 mono, sample_rate : 16000 로 파일변환

import librosa
# 변환할 파일 불러옴(모노,16000으로 변환해서)
data,sr = librosa.load('/Users/hbk/downloads/myRecording01.wav', mono=True, sr=16000)

# 변환된 파일을 저장
librosa.output.write_wav(
    "/Users/hbk/downloads/hello.wav", data, rate  # 변환된 파일
)


