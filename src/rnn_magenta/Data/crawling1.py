from bs4 import BeautifulSoup     #BeautifulSoup 임포트
from selenium import webdriver     #셀레니움 임포트
from selenium.webdriver.common.keys import Keys     # 스크롤 내리기
import time
import csv

#driver = webdriver.PhantomJS('c:/python/phantomjs') #팬텀js 드라이버 경로 선언
driver = webdriver.Chrome("c:/python/chromedriver") # 크롬 드라이버는 경로 설정 해주어야 해요~
                                                    
driver.get('https://freemidi.org/genre-pop')     # youtube 주소
driver.implicitly_wait(10)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')
url1 = []     # 리스트 형으로 url 복사
title = {}


print("url 복사 시작합니다 잠시만 기다려주세요^^")


for i in soup.select('span > a[href]'):
                     url1.append("https://freemidi.org/"+i.attrs['href'])

url1 = url1[60:-9]

driver = webdriver.Chrome("c:/python/chromedriver") 
url2 = []
for i in url1[:3]:
    driver.get(i)     # youtube 주소
    soup = BeautifulSoup(driver.page_source, 'html.parser')  
    
    for j in soup.select('#mainContent > div > div > div > div > div > span > a[href]'):
        url2.append("https://freemidi.org/"+j.attrs['href'])
        
        

driver = webdriver.Chrome("c:/python/chromedriver") 
for i in url2:
    driver.get(i)          
    soup = BeautifulSoup(driver.page_source, 'html.parser')  
    
    driver.find_element_by_xpath('//*[@id="downloadmidi"]').click()
