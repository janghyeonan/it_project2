# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:35:52 2018

@author: STU
"""

##############
## url 복사 ##
#############


# def youtubeurl(url,num):       # 함수(주소,스크롤 내리기 수, 드라이버 파일 위치, 경로+파일명.csv)
    
from bs4 import BeautifulSoup     #BeautifulSoup 임포트
from selenium import webdriver     #셀레니움 임포트
from selenium.webdriver.common.keys import Keys     # 스크롤 내리기
import time
import csv
    
#driver = webdriver.PhantomJS('c:/python/phantomjs') #팬텀js 드라이버 경로 선언
driver = webdriver.Chrome("c:/python/chromedriver") # 크롬 드라이버는 경로 설정 해주어야 해요~
    
driver.get('https://www.youtube.com/channel/UCsEonk9fs_9jmtw9PwER9yg/videos')     # youtube 주소
driver.implicitly_wait(10)
    
body = driver.find_element_by_tag_name("body")
    
num_of_pagedowns = 200            # 스크롤 내기리 설정
    
print("대량파일 추출을 위해 스크롤 내리고 있는 중입니다 잠시만 기다려 주세요^^")
    
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)
    num_of_pagedowns -= 1
    
soup = BeautifulSoup(driver.page_source, 'html.parser')
url1 = []     # 리스트 형으로 url 복사
title = {}      # 데이터를 넣을 딕셔너리 선언 / key:제목, val:조회수
    
    
print("url 복사 시작합니다 잠시만 기다려주세요^^")
    
for i in soup.select('#video-title'):
                     url1.append("https://www.youtube.com"+i.attrs['href'])
                     title[i.attrs['title']]=i.attrs['aria-label'][i.attrs['aria-label'].rfind(' ')+1:-1]
    
print('< 총 '+str(len(url1))+'개의 url 이 복사 되었습니다. >')
    
    



#################################
## mp3 파일정보 csv 데이터 추출 ##
################################

def csvfile(save,filename):  # csvsave(저장경로, 파일명)

    import csv
    w=csv.writer(open(str(save)+'/'+str(filename)+".csv", "w"))
    for r in title.items():
        w.writerow(r)
    print(str(filename)+'.csv 파일명으로 '+str(save)+' 경로에 저장 되었습니다.')
        

"""
ex)
csvfile('c:/python','아이돌')
"""

#######################
#  mp3 파일 변환 추출  #
#######################

def mp3output(url1,indexnum=0):      # mp3output(변환 주소,남은 url number)
    #mp3url="https://www.flvto.biz/kr/downloads/mp3/yt_elRqTV6wUaM/"     # mp3변환 사이트
    driver = webdriver.Chrome("c:/python/chromedriver")
    driver.get('https://www.flvto.biz/kr/downloads/mp3/yt_elRqTV6wUaM/')
    
    
    long2 = len(url1[indexnum:])
    
    for j in url1:
        inputid = driver.find_element_by_id("convertUrl")   # id 값 입력
        inputid.clear()     # 입력박스에 있는 텍스트 지우기
        driver.implicitly_wait(3)
        print("url 입력")
        inputid.send_keys(j)  # 유튜브 url 주소 입력
        print("MP3 변환")
        driver.find_element_by_xpath('//*[@id="convertForm"]/div[2]/button').click()
        driver.implicitly_wait(30)
        print("다운로드")
        driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/div[2]/div[1]/a[1]').click()
    
    
    
    # 뒤로가기 두번
        driver.implicitly_wait(10)
        driver.back()
        driver.implicitly_wait(10)
        driver.back()
    
        long2 -= 1
        print(str(long2)+'개 남음')
    
    driver.close()



# 추출 데이터 youtube
'''
발라드
https://www.youtube.com/channel/UCrwx6JRz13tkmfNvc9iLhMw/videos

힙합
https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/videos

락음악
https://www.youtube.com/channel/UCRZoK7sezr5KRjk7BBjmH6w/videos

EDM
https://www.youtube.com/user/NoCopyrightSounds/videos
"""
