#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 14:42:14 2018

@author: hbk
"""

with open('/Users/hbk/data/text.txt','r') as f:
    text = f.read()  # txt파일 전체를 하나의 문자로 읽어드림
text


from konlpy.tag import Twitter
t = Twitter()
print(t.morphs(text))

text_list = t.morphs(text)

text_dict = {}
for i in text_list:
    if i in text_dict.keys():
        text_dict[i] += 1
    else:
        text_dict[i] = 1
text_dict

text_sort = sorted(text_dict.items(), reverse = True, key = lambda x : x[1]) 
text_sort


import re
# OOO OOO OOO니다 또는 OOO니다 찾기
m = re.findall("\w+\s\w+\s\w+니다|\w+니다", text) # https://wikidocs.net/4308#_3 참조
print(m)

s = re.findall("\w+니다", text)


s1 = []
for i in s:
    s1 = re.sub('니다','',i) 
    #s2 = t.nouns(i)
    print(s1)


s2 = re.findall("\p였습니다", text)
print(s2)

m = re.search('[a-z]+', "python")[0]
print(m)




import re 

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

p = re.compile('Crow|Servo')
m = p.match('CrowHello')

m = re.match('Crow|Serve', 'CrowHello')
print(m[0])


## softmax 

import tensorflow as tf

X = tf.placeholder(tf.float32, [None, 128])
Y = tf.placeholder(tf.int32, [None, 1])  

Y_one_hot = tf.one_hot(Y, 4)  # 감정 4가지
Y_one_hot = tf.reshape(Y_one_hot, [-1, 4]) 

W1 = tf.Variable(tf.random_normal([128, 4]), name='weight1')
b1 = tf.Variable(tf.random_normal([4]), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X,W1)+b1)

W2 = tf.Variable(tf.random_normal([4, 4]), name='weight2')
b2 = tf.Variable(tf.random_normal([4]), name='bias2')
layer2 = tf.nn.tanh(tf.matmul(layer1,W2)+b2)

W3 = tf.Variable(tf.random_normal([4, 4]), name='weight2')
b3 = tf.Variable(tf.random_normal([4]), name='bias2')
layer3 = tf.matmul(layer2,W3)+b3

#logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(layer3)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=layer3,labels=Y_one_hot))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.Session() # session open
sess.run(tf.global_variables_initializer())

for step in range(7001):
    sess.run(optimizer, feed_dict={X: x_train, Y: y_train})
    if step % 1000 == 0:
        loss, acc = sess.run([cost, accuracy], feed_dict={ X: x_train, Y: y_train})
        print("Step: {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format( step, loss, acc))


pred = sess.run(prediction, feed_dict={X: x_test})
acc = sess.run(accuracy, feed_dict={X: x_test, Y: y_test})
print(acc)

# 17:43 마지막 은닉층에서 항등으로 내보내니 결과 좋아짐

sess.close() # session close

import sys
sys.path.append('/Users/hbk/github/it_project2/TH/')

import mlpcPre
mlpcPre.main('/Users/hbk/data/python-docs-samples/speech/cloud-client/sampling_cut/8_3_N.wav')
