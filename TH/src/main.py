#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import librosa
import numpy as np
from sklearn.neural_network import MLPClassifier  # 다중분류에 해당되는 패키지 사용

# 음성파일 경로
path = '/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/' 


# 감정분석할 음성파일
sound_path = '/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/10_6_N.wav'  


## 음성파일 melspectrogram으로 분석된 값으로 리턴

def arrayStack(path): # input : 경로값 (ex. 'Users/.../')
    files = os.listdir(path) # 해당경로 폴더에 담긴 wav 파일목록 저장
    x = np.arange(128)
    y = np.arange(1)
    
    for i in files:
        label = i.split('.')[0].split('_')[-1] # 파일명에서 감정부분 추출 -> 숫자로 임의부여
                
        if label == 'S': # 슬픔
            l = 0
        elif label == 'N': # 중립
            l = 1
        elif label == 'J': # 즐거움
            l = 2
        elif label == 'A': # 화남
            l = 3   
  
        r,sr = librosa.load(path+i, mono=True, sr=16000) # librosa 사용(모노, 샘플레이트 : 16000)
        mel = librosa.feature.melspectrogram(y=r, sr=sr) # 음성에는 melspectrogram이 좋다고 해서 
        a = np.mean(mel,axis=1) # 열 중간값 구함
        
        x = np.vstack([x,a]) # 적재
        y = np.vstack([y,np.array(l)]) # 적재
        
    return x[1:], y[1:]



## 훈련 및 테스트 데이터셋 세팅
    
def dataSet(x,y): # x : 데이터값, y : 라벨값
    n = len(x)
    import random
    train_index = random.sample(range(n),int(n*0.8))
    test_index = [i for i in range(n) if i not in train_index]
    
    from sklearn.preprocessing import normalize
    # 훈련데이터는 전체데이터 80% 랜덤 추출
    x_train = normalize(x[train_index]) 
    y_train = y[train_index]
    # 테스트데이터는 전체데이터 20% 랜덤 추출
    x_test = normalize(x[test_index])
    y_test = y[test_index]
    
    return x_train, y_train, x_test, y_test 


## 데이터 분석(MLPClassifier)

def mlpc(x,y): # 훈련 및 검증결과 출력이후 모델을 리턴
    
    x_train, y_train, x_test, y_test = dataSet(x,y)
    
    # 훈련을 통해 모델을 생성
    mlp_multilabel = MLPClassifier(hidden_layer_sizes=(128,128), max_iter=1000, random_state=None).fit(x_train, y_train)
    acc1 = mlp_multilabel.score(x_train, y_train) # 정확도
    print('\n모델 정확도 :',acc1)

    # 모델 검증
    y_pred = mlp_multilabel.predict(x_test)
    print('모델 검증 :',np.sum(np.sum(y_test.astype(int) & y_pred, axis=1) > 0)/y_test.shape[0])
    
    return mlp_multilabel # 모델


## 감정 예측
    
def dataMake(sound_path): # input : 음성파일이 담겨있는 파일경로 ex. "/Users/.../sori.wav"
    # 음성데이터 분석    
    r,sr = librosa.load(sound_path, mono=True, sr=16000) # librosa 사용(모노, 샘플레이트 : 16000)
    mel = librosa.feature.melspectrogram(y=r, sr=sr)
    #mfcc = librosa.feature.mfcc(r,sr)
    a = np.mean(mel,axis=1) # 열 평균값 구함
    
    from sklearn.preprocessing import normalize
    data = normalize(a.reshape(1,128))
    
    return data

  
def pred(model,sound_path):
    pred1 = model.predict(dataMake(sound_path))  # mlpc()에서 생성된 모델에 의한 예측값

    for i in pred1:
        if i == 0:
            res = "슬픔"
        elif i == 1:
            res = "중립"
        elif i == 2:
            res = "기쁨"
        elif i == 3:
            res = "화남"
    return res


## 메인함수
    
def main(): 
    global path, sound_path
    x,y = arrayStack(path)
    x_train, y_train, x_test, y_test = dataSet(x,y)
    model = mlpc() # 모델생성
    return pred(model, sound_path)
 
    

if __name__ == '__main__':
    
    print('감정결과 :',main())    

 