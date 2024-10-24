from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options
import pyautogui
import re

# url = "https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL"
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)
# pyautogui.moveTo(1270,550)
# time.sleep(1)
# pyautogui.moveTo(1270,480)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(200,800)
# time.sleep(1)
# prev_height = browser.execute_script("return articleListArea.scrollHeight")
# print("화면 높이 : ",prev_height)
# while True:
#   # browser.execute_script("window.scroll(0,articleListArea.scrollHeight)")
#   pyautogui.scroll(-prev_height)
#   time.sleep(2)
#   curr_height = browser.execute_script("return articleListArea.scrollHeight")
#   if prev_height == curr_height: break
#   prev_height = curr_height
#   print("높이 : ",prev_height)
# # print("-"*50)
# # all_height = browser.execute_script("return document.body.scrollHeight")
# # print("화면 전체 높이 : ",all_height)
# soup = BeautifulSoup(browser.page_source,"lxml")
# data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")
# with open("c1024/naver.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())

# 매매 낮은 5개, 전세가격이 낮은 5개를 출력하시오.


bargain = []
monthly_rent_list = []
charter_list = []

# input("엔터키 입력완료")

soup = None
with open("c1024/naver.html","r",encoding="UTF-8") as f:
  soup = BeautifulSoup(f,"lxml")

data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")

items = data.select(".item")

for item in items:
  name = item.select_one(".item_title").text.strip()
  area_type = item.select_one(".info_area p span.spec").text.strip()
  area_type = int(re.search(r"^[1-9]+(?=[a-zA-Z\/])",area_type).group())
  price_line = item.select_one(".price_line")
  price_type = price_line.select_one(".type").text.strip()
  prices = price_line.select_one(".price").text.strip()
  price_tail = ""
  if prices.find("/") != -1:
    tmp = list(map(lambda x:x.strip(),prices.split("/")))
    prices = tmp[0]
    price_tail = tmp[1]
  
  prices = prices.split(" ")
  price = int(f"{prices[0][:-1]}{int(prices[1].replace(",","")):04}0000") if prices[0].find("억") != -1 and len(prices)>1 else int(f"{prices[0][:-1]}00000000") if prices[0].find("억") != -1 else int(prices[0].replace(",",""))

  # print(price_type,f"{price} / {price_tail}" if len(price_tail)>0 else price)

  h = {"name": name,"price_type":price_type,"price":price,"ptail":price_tail,"area_type":area_type}
  if price_type == "월세":
    monthly_rent_list.append(h)
  elif price_type == "전세":
    charter_list.append(h)
  elif price_type == "매매":
    bargain.append(h)

bargain.sort(key=lambda x:x["price"])
monthly_rent_list.sort(key=lambda x:x["price"])
charter_list.sort(key=lambda x:x["price"])


print("[ 매매 ]")
for h in bargain[:5]:
  print("이름 :",h["name"])
  print("매매타입 :",h["price_type"])
  print("전용면적 :",h["area_type"])
  print("가격 :",h["price"],end="")
  print(f"/{h["ptail"]}" if len(h["ptail"]) > 0 else "")
print("-"*50)

print("[ 전세 ]")
for h in charter_list[:5]:
  print("이름 :",h["name"])
  print("매매타입 :",h["price_type"])
  print("전용면적 :",h["area_type"])
  print("가격 :",h["price"],end="")
  print(f"/{h["ptail"]}" if len(h["ptail"]) > 0 else "")
print("-"*50)

print("[ 월세 ]")
for h in monthly_rent_list[:5]:
  print("이름 :",h["name"])
  print("매매타입 :",h["price_type"])
  print("전용면적 :",h["area_type"])
  print("가격 :",h["price"],end="")
  print(f"/{h["ptail"]}" if len(h["ptail"]) > 0 else "")
print("-"*50)