#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip3 install librosa
import librosa
import os
import numpy as np

## 녹음파일 샘플들 array 형으로 적재하는 함수

def arrayStack(path): # input : 경로값 (ex. 'Users/.../')
    files = os.listdir(path) # 해당경로 폴더에 담긴 wav 파일목록 저장
    x = np.arange(20)
    y = np.arange(1)
    
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
        
        r,sr = librosa.load(path+i) # librosa 사용
        mfcc = librosa.feature.mfcc(r,sr)
        a = np.mean(mfcc,axis=1) # 열 평균값 구함
        
        x = np.vstack([x,a]) # 적재
        y = np.vstack([y,np.array(l)]) # 적재
        
    return x, y

#x,y = arrayStack('/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/')


x_train = x[1:128]
y_train = y[1:128]

x_test = x[128:]
y_test = y[128:]


## 데이터프레임 넣기
import pandas as pd
from pandas import DataFrame,Series

X = DataFrame(x[1:])
Y = DataFrame(y[1:])
pd.merge(X,Y,left_index = True, right_index=True)


## softmax 

import tensorflow as tf

X = tf.placeholder(tf.float32, [None, 20])
Y = tf.placeholder(tf.int32, [None, 1])  

Y_one_hot = tf.one_hot(Y, 4)  # 감정 4가지
Y_one_hot = tf.reshape(Y_one_hot, [-1, 4]) 

W = tf.Variable(tf.random_normal([20, 4]), name='weight')
b = tf.Variable(tf.random_normal([4]), name='bias')

logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y_one_hot))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(cost)

prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session() # session open
sess.run(tf.global_variables_initializer())

for step in range(7001):
    sess.run(optimizer, feed_dict={X: x_train, Y: y_train})
    if step % 100 == 0:
        loss, acc = sess.run([cost, accuracy], feed_dict={ X: x_train, Y: y_train})
        print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format( step, loss, acc))


pred = sess.run(prediction, feed_dict={X: x_test})
pred
acc = sess.run(accuracy, feed_dict={X: x_test, Y: y_test})
acc 
sum(pred == y_test.reshape(33,))/33

pred = sess.run(prediction, feed_dict={X: x_test[[2]]})
acc = sess.run(accuracy, feed_dict={X: x_test[[2]], Y: y_test[[2]]})

if pred[0] == 0:
    print("감정 : %s, 정확도 : %.2f" %("슬픔",acc))
elif pred[0] == 1:
    print("감정 : %s, 정확도 : %.2f" %("중립",acc))
elif pred[0] == 2:
    print("감정 : %s, 정확도 : %.2f" %("기쁨",acc))
elif pred[0] == 3:
    print("감정 : %s, 정확도 : %.2f" %("화남",acc))

# 84% 까지 나옴
sess.close() # session close

