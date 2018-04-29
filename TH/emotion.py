#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip3 install librosa
import librosa
import os
import numpy as np

## 녹음파일 샘플들 array 형으로 적재
files = os.listdir('/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/') #파일명 불러오기
x = np.arange(20) # mfcc 평균낸 값 담을 곳
y = np.arange(1) # lable 값 담을 곳

for i in files:
    label = i.split('.')[0].split('_')[2] # 파일명에서 감정부분 추출 -> 숫자로 임의부여
    if label == 'S': # 슬픔
        l = 0
    elif label == 'N': # 중립
        l = 1
    elif label == 'J': # 즐거움
        l = 2
    elif label == 'A': # 화남
        l = 3
    
    r,sr = librosa.load('/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/'+i)
    mfcc = librosa.feature.mfcc(r,sr)
    a = np.mean(mfcc,axis=1) # 열기준 평균 (행기준하면 파일마다 열이 다르게 나와서 이렇게 함)
    
    x = np.vstack([x,a]) # 적재
    y = np.vstack([y,np.array(l)]) # 적재

## 데이터프레임 넣기
import pandas as pd
from pandas import DataFrame,Series

X = DataFrame(x[1:])
Y = DataFrame(y[1:])
pd.merge(X,Y,left_index = True, right_index=True)


## Logistic regression
#pip install sklearn

from sklearn import linear_model 

x_train = x[1:60]
y_train = y[1:60]
x_train.shape
y_train.shape

x_test = x[60:]
y_test = y[60:]


logreg = linear_model.LogisticRegression()
logreg.fit(x_train, y_train)
y_test_estimated = logreg.predict(x_test)
y_test_estimated.shape # (101,)

sum(y_test_estimated == y_test.reshape(101,))/101  # 정확도


#np.array(0)
#np.ndarray(0)
#np.zeros(0)    
#np.arange(0)