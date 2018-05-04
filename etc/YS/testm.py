# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 19:54:52 2018

@author: STU
"""
#1차 멜로디 생성 테스트
# 멜로디를 생성하는 우분투 터미널 명령어를 쉘 스크립트로 저장한 후
import os, sys # 모듈을 불러온다 
os.system("/bin/sh /home/ys/testm.sh") 
#쉘 스크립트를 불러온다 리턴값이 0일 경우에만 정상적인 결과가 나온다. 
#더 나은 방법이 있으면 수정할 예정
