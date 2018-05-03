#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import librosa
import numpy as np
from sklearn.neural_network import MLPClassifier  # 다중분류에 해당되는 패키지 사용
import random
from sklearn.preprocessing import normalize
import pandas as pd

## 훈련 및 테스트 데이터셋 세팅 (모델값)
def dataMake(): # input : 음성파일이 담겨있는 파일경로 ex. "/Users/.../sori.wav"
    # 음성데이터 분석    
    r,sr = librosa.load('/Users/janghyeonan/flask/tmp/sound.wav', mono=True, sr=16000) # librosa 사용(모노, 샘플레이트 : 16000)
    mel = librosa.feature.melspectrogram(y=r, sr=sr)
    #mfcc = librosa.feature.mfcc(r,sr)
    a = np.mean(mel,axis=1) # 열 평균값 구함    
    z = normalize(a.reshape(1,128))
    return z

#모델스
## 훈련 및 테스트 데이터셋 세팅 (모델값)
def models():
    x = pd.read_csv("/Users/janghyeonan/flask/model/x_data.csv", index_col = 0).values
    y = pd.read_csv("/Users/janghyeonan/flask/model/y_data.csv", index_col = 0).values
    z = dataMake()
    
    n = len(x)
    
    train_index = random.sample(range(n),int(n*0.8))
    test_index = [i for i in range(n) if i not in train_index]
        
    # 훈련데이터는 전체데이터 80% 랜덤 추출
    x_train = normalize(x[train_index]) 
    y_train = y[train_index]
    
    # 테스트데이터는 전체데이터 20% 랜덤 추출
    x_test = normalize(x[test_index])
    y_test = y[test_index]    
    
    # 훈련을 통해 모델을 생성
    mlp_multilabel = MLPClassifier(hidden_layer_sizes=(128,128), max_iter=1000, random_state=None).fit(x_train, y_train)
    acc1 = mlp_multilabel.score(x_train, y_train) # 정확도
    #print('\n모델 정확도 :',acc1)

    # 모델 검증
    y_pred = mlp_multilabel.predict(x_test)
    #print('모델 검증 :',np.sum(np.sum(y_test.astype(int) & y_pred, axis=1) > 0)/y_test.shape[0])      
    
    #예측 데이터 진행
    pred1 = mlp_multilabel.predict(z)  # mlpc()에서 생성된 모델에 의한 예측값
    
    #숫자를 감정텍스트로 변환
    for i in pred1:
        if i == 0:
            res = "슬픔"
        elif i == 1:
            res = "중립"
        elif i == 2:
            res = "기쁨"
        elif i == 3:
            res = "화남"
    return res,acc1

if __name__ == '__main__':    
        print('감정결과 :', models())