
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup     #BeautifulSoup 임포트
from selenium import webdriver     #셀레니움 임포트
from selenium.webdriver.common.keys import Keys     # 스크롤 내리기
import time
import csv

#driver = webdriver.PhantomJS('c:/python/phantomjs') #팬텀js 드라이버 경로 설정
driver = webdriver.Chrome("c:/python/chromedriver") # 크롬 드라이버는 경로 설정 
                                                    
driver.get('https://www.freemidi.org/genre-hip-hop-rap') #freemidi 주소
driver.implicitly_wait(10)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
url1 = []     # 리스트 형으로 url 복사



print("url 복사 시작합니다 잠시만 기다려주세요^^")

#가수들 url주소 수집
for i in soup.select('a[href]'): 
    url1.append("https://freemidi.org/"+i.attrs['href'])
    
print('< 총 '+str(len(url1))+'개의 url 이 복사 되었습니다. >')

url1 = url1[60:-9] #url 주소 앞뒤로 정제!


#가수들에 대한 곡 url주소 수집
url2 = []
driver = webdriver.Chrome("c:/python/chromedriver")
for j in url1:
    driver.get(j)     
    soup = BeautifulSoup(driver.page_source, 'html.parser')  
    for i in soup.select('#mainContent > div > div > div > div > div > span > a[href]'):
        url2.append("https://freemidi.org/"+i.attrs['href'])
        
        
#곡 다운로드 작업
driver = webdriver.Chrome("c:/python/chromedriver") 
for i in url2:
    driver.get(i)          
    soup = BeautifulSoup(driver.page_source, 'html.parser')  
    
    driver.find_element_by_xpath('//*[@id="downloadmidi"]').click()
