from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

url = "http://www.daum.net"

# 크롬 브라우저 열기
browser = webdriver.Chrome()
# 다음 페이지 이동
browser.get(url)

elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()

id = "aaaa@kakao.com"
pw = "1111"
js_script = f'''
  document.getElementById("loginId--1").value = "{id}";
  document.getElementById("password--2").value = "{pw}";
'''
browser.execute_script(js_script)

# 대기
time.sleep(random.randint(2,5))
# 클릭
elem = browser.find_element(By.CLASS_NAME,"btn_g")
elem.click()

time.sleep(10)