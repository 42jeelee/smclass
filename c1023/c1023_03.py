from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
browser.get("https://naver.com")

# html위치 찾기 - requests:select
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()      # 클릭
browser.back()    # 뒤로가기
browser.forward() # 앞으로가기
browser.refresh() # 새로고침
elem = browser.find_element(By.NAME,"pw")

elem = browser.find_element(By.ID,"query")
elem.send_keys("네이버 영화")
# enter키 입력
elem.send_keys(Keys.ENTER)
# 클릭
elem.click()

# 새창이동
browser.switch_to.window(browser.window_handles[1])

time.sleep(10)
