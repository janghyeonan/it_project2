#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip3 install librosa
import librosa
import os
import numpy as np
import tensorflow as tf


path = '/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/' # 음성파일 저장된 폴더경로
model_path = "/Users/hbk/data/model/"
    
    
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
        a = np.mean(mfcc,axis=1) # 열 중간값 구함
        
        x = np.vstack([x,a]) # 적재
        y = np.vstack([y,np.array(l)]) # 적재
        
    return x[1:], y[1:]



## 훈련데이터, 테스트데이터 세팅하는 함수

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



## model 생성

def emotionModel(x_train,y_train,model_path): # model_path : model 저장할 위치 입력
    X = tf.placeholder(tf.float32, [None, 20])
    Y = tf.placeholder(tf.int32, [None, 1])  
    
    Y_one_hot = tf.one_hot(Y, 4)  # 감정 4가지
    Y_one_hot = tf.reshape(Y_one_hot, [-1, 4]) 
    
    W = tf.Variable(tf.random_normal([20, 4]), name='weight1')
    b = tf.Variable(tf.random_normal([4]), name='bias1')

    logits = tf.matmul(X, W) + b
    hypothesis = tf.nn.softmax(logits)
    
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y_one_hot))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(cost)
    #optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
    
    prediction = tf.argmax(hypothesis, 1)
    correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    saver = tf.train.Saver() # 저장 선언
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for step in range(7001):
            sess.run(optimizer, feed_dict={X: x_train, Y: y_train})
            if step % 100 == 0:
                loss, acc = sess.run([cost, accuracy], feed_dict={ X: x_train, Y: y_train})
                print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format( step, loss, acc))
        
        save_path = saver.save(sess, model_path+'emotion_model') # 최종 학습된 모델 저장

    print("Model saved in file: %s" % save_path)

    return save_path




## model 검증
def modelTest(x_test,y_test,save_path):
    X = tf.placeholder(tf.float32, [None, 20])
    Y = tf.placeholder(tf.int32, [None, 1])  
    
    Y_one_hot = tf.one_hot(Y, 4)  # 감정 4가지
    Y_one_hot = tf.reshape(Y_one_hot, [-1, 4]) 
    
    W = tf.Variable(tf.random_normal([20, 4]), name='weight1')
    b = tf.Variable(tf.random_normal([4]), name='bias1')

    logits = tf.matmul(X, W) + b
    hypothesis = tf.nn.softmax(logits)
    
    prediction = tf.argmax(hypothesis, 1)
    correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    saver_new = tf.train.Saver() # 저장 선언

    with tf.Session() as sess:
        # 기존 저장된 모델을 불러온다
        sess.run(tf.global_variables_initializer())
        saver_new = tf.train.import_meta_graph(save_path+".meta")  # 모델저장경로
        saver_new.restore(sess, save_path)  
        tf.get_default_graph().as_graph_def()

        print("예측결과")
      
        # 모델을 사용하여 작업    
        pred = sess.run(prediction, feed_dict={X: x_test})  # 기존 학습모델에 의해 나온 예측값
        acc = sess.run(accuracy, feed_dict={X: x_test, Y: y_test})  # 실제와 비교 (정확도)
        for i in pred:
            if i == 0:
                print("감정 : %s" %"슬픔")
            elif i == 1:
                print("감정 : %s" %"중립")
            elif i == 2:
                print("감정 : %s" %"기쁨")
            elif i == 3:
                print("감정 : %s" %"화남")
        print("정확도 : %.2f" %acc)
      

 

if __name__ == '__main__':

    x,y = arrayStack(path)
    x_train,y_train,x_test,y_test = dataSet(x,y)
    
    tf.reset_default_graph() 
    save_path = emotionModel(x_train,y_train,model_path)
    tf.reset_default_graph() 
    modelTest(x_test,y_test,save_path)

