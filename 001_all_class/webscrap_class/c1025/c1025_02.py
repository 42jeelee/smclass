from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv

# # 파일저장하기
# browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(1,6):
#   url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
#   browser.get(url)
#   time.sleep(2)
#   # # 화면을 스크롤해서 내리기 반복
#   prev_height = browser.execute_script("return document.body.scrollHeight")
#   while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     WebDriverWait(browser,10).until(lambda x:x.find_element(By.XPATH,'//*[@id="content"]/div[1]'))

#     # 페이지가 로딩되면서 길어진 길이를 다시 가져옴.
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
#     if prev_height == curr_height:
#       break
#     # 더 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
#     prev_height = curr_height
#   print("스크롤 내리기 완료")
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   with open(f'c1025/navershop{i}.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
#   time.sleep(2)
# browser.close()
# 2.
# 제목,금액,평점,평가수,찜 정보를 1-5페이지까지 가져와서
# 평점 4.8이상, 평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.

def format_rank_num(rank_num):
  rank_num = rank_num.replace("\n","").replace("\t","").replace(" ","").replace("(","").replace(")","")
  if rank_num.find("만") != -1:
    d = rank_num.find(".") if rank_num.find(".") != -1 else 0
    return rank_num.replace(".","")[:-1] + "0000"[d:]
  return rank_num.replace(",","")

search_list = []

for i in range(1,6):
  soup = ""
  with open(f"c1025/navershop{i}.html","r",encoding="UTF-8") as f:
    soup = BeautifulSoup(f,"lxml")
  
  data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div")

  items = data.select('&>div')
  for item in items:
    name = item.select_one('div[class*="_title_"]>a').text.strip()
    price = item.select_one('div[class*="_price_area_"] span.price em').text.strip()
    price = int(price.replace(",",""))
    etc_box = item.select_one('div[class*="_etc_box_"]')
    
    rank = etc_box.select_one('span[class*="adProduct_rating"]')
    if rank is None: rank = etc_box.select_one('.product_grade__IzyU3')
    if rank is not None:
      rank = rank.text.strip()
      if rank.find("별점")!=-1: rank = rank.replace("\n","").split(" ")[-1]
      rank = float(rank)
    
    rank_num = etc_box.select_one('span[class*="adProduct_count"]')
    if rank_num is None: rank_num = etc_box.select_one('.product_num__fafe5')
    if rank_num is not None:
      rank_num = int(format_rank_num(rank_num.text.strip()))

    wish_list = etc_box.select_one("&>span>span")
    if wish_list is not None: wish_list = int(wish_list.text.strip().replace(",",""))

    if rank is None or rank_num is None: continue
    if rank < 4.9 or rank_num < 1000: continue

    i = {
      "name":name,
      "price": price,
      "rank":rank if rank is not None else "(없음)",
      "rank_num":rank_num if rank_num is not None else "(없음)",
      "wish_list":wish_list if wish_list is not None else "(없음)"
    }
    search_list.append(i)

search_count = len(search_list)
if search_count > 0:
  with open("c1025/nshop.csv","w",encoding="UTF-8",newline="") as f:
    writer = csv.writer(f)

    print(f"search count: {search_count}")

    writer.writerow(list(search_list[0].keys()))  

    for i in search_list:
      print(f"[ {i["name"]}, {i["price"]}, {i["rank"]}, {i["rank_num"]}, {i["wish_list"]} ]")
      writer.writerow(list(i.values()))