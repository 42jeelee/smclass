# gmarket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options

# 노트북 검색 된 사이트에서 1,2,3페이지 에서
# 만족도 95 이상이면서, 평가수 100이상, 금액 1500000이하

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

# 페이지 생성
for i in range(1,4):
  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i}"

  browser = webdriver.Chrome(options=options)
  browser.maximize_window()
  browser.get(url)

  WebDriverWait(browser,20).until(lambda x:x.find_element(By.XPATH,'//*[@id="section__inner-content-body-container"]/div[4]/div[1]'))

  browser.get_screenshot_as_file(f"c1024/gmarket{i}.png")
  soup = BeautifulSoup(browser.page_source,"lxml")

  browser.close()

  with open(f"c1024/gmarket{i}.html","w",encoding="UTF-8") as f:
    f.write(soup.prettify())

# 페이지 불러오기
search_list = []
for i in range(1,4):
  soup = None
  with open(f"c1024/gmarket{i}.html","r",encoding="UTF-8") as f:
    soup = BeautifulSoup(f,"lxml")
  
  datas = soup.select("div.box__component-itemcard")
  print(len(datas))

  for idx,data in enumerate(datas):
    item = data.select_one("div.box__item-container")
    name = item.select_one("span.text__item").text.strip()
    rank_num = item.select_one("li.list-item__feedback-count text")
    if rank_num is not None: rank_num = rank_num.text.strip()
    price = item.select_one("div.box__price-sale>strong")
    satisfaction = item.select_one("span.image__awards-points")
    if satisfaction is not None: satisfaction = int(satisfaction.text.strip()[4:6])
    if price is None: price = item.select_one("div.box__price-seller>strong")
    if price is not None: price = int(price.text.strip().replace(",",""))

    if satisfaction is None or price is None: continue
    if satisfaction < 95 or price > 1500000: continue

    print("제품명 :", name)
    print("평가수 :", rank_num)
    print("가격 :", price)
    print("만족도 :", satisfaction)
    print("-"*80)
