#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#텐서 플로우를 이용한 모델이었으나, 이번 프로젝트에서는 사용되지 않았다.
import librosa
import numpy as np
import tensorflow as tf

path = '/Users/janghyeonan/flask/tmp/sound.wav'
save_path = '/Users/janghyeonan/flask/model/emotion_model'


## 훈련데이터, 테스트데이터 세팅하는 함수

def dataMake(path): # input : 음성파일이 담겨있는 파일경로 ex. "/Users/.../sori.wav"
    # 음성데이터 분석    
    r,sr = librosa.load(path) # librosa 사용
    mfcc = librosa.feature.mfcc(r,sr)
    a = np.mean(mfcc,axis=1) # 열 평균값 구함
    
    from sklearn.preprocessing import normalize
    data = normalize(a.reshape(1,20))
    
    return data


## 기존의 훈련모델을 불러와서 결과값 예측(감정예측)

def emotionPre(data,save_path): # data : dataMake(), save_path : 학습모델 저장된 경로 및 모델명
    X = tf.placeholder(tf.float32, [None, 20])

    W = tf.Variable(tf.random_normal([20, 4]), name='weight1')
    b = tf.Variable(tf.random_normal([4]), name='bias1')

    logits = tf.matmul(X, W) + b
    hypothesis = tf.nn.softmax(logits)
    prediction = tf.argmax(hypothesis, 1)
    
    saver_new = tf.train.Saver() # 기존 모델로 초기화
    
    with tf.Session() as sess:
        # 기존 저장된 모델을 불러온다
        saver_new = tf.train.import_meta_graph(save_path+".meta")  # 모델저장경로
        saver_new.restore(sess, save_path)
        # 모델을 사용하여 작업    
        pred = sess.run(prediction, feed_dict={X: data})  # 기존 학습모델에 의해 나온 예측값
        res = ''
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

def main():
    tf.reset_default_graph()
    return emotionPre(dataMake(path),save_path)
 
if __name__ == '__main__':
    print('예측된 감정 :',main())