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
