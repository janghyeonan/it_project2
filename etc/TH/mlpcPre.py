#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import numpy as np

code_path = '/Users/hbk/github/it_project2/TH/' # import 할 코드있는 폴더경로
sound_path = '/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/' # 음성파일 경로


sys.path  # 경로확인 만든 파일 불러와서 사용하려고
sys.path.append(code_path) # 경로 추가


from emotion import arrayStack, dataSet  # emotion.py에서 만든 함수를 불러옴
x,y = arrayStack(sound_path) # 해당경로의 폴더에 있는 음성파일을 librosa의 melspectrogram으로 분석
x_train, y_train, x_test, y_test = dataSet(x,y) # 훈련 80%, 테스트 20%  


## 데이터 분석(MLPClassifier)

def mlpc(): # 훈련 및 검증결과 출력이후 모델을 리턴
    from sklearn.neural_network import MLPClassifier  # 다중분류에 해당되는 패키지 사용
    global x_train, y_train, x_test, y_test 
    
    # 훈련을 통해 모델을 생성
    mlp_multilabel = MLPClassifier(hidden_layer_sizes=(128,128), max_iter=1000, random_state=None).fit(x_train, y_train)
    acc1 = mlp_multilabel.score(x_train, y_train) # 정확도
    print('\n모델 정확도 :',acc1)

    # 모델 검증
    y_pred = mlp_multilabel.predict(x_test)
    print('모델 검증 :',np.sum(np.sum(y_test.astype(int) & y_pred, axis=1) > 0)/y_test.shape[0])
    
    return mlp_multilabel # 모델


## 감정 예측함수
    
def pred(model,data):
    from emotionPre import dataMake
    pred = model.predict(dataMake(data))  # mlpc()에서 생성된 모델에 의한 예측값

    for i in pred:
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
    
def main(data): # mlpc(), pred() 둘다 실행해서 감정값 리턴
    model = mlpc() # 모델생성
    return pred(model, data)
 
    

if __name__ == '__main__':
    data = '/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/10_6_N.wav'  # 임의지정(변동바람)
    print('감정결과 :',main(data))    

# 다른 곳에서 사용
#import mlpcPre
#l.main('/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/8_3_N.wav')    
    
