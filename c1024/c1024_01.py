from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import random

# url = "https://www.yanolja.com/"
# # 브라우저 열기
# browser = webdriver.Chrome()
# # 창 최대화
# browser.maximize_window()
# # url입력
# browser.get(url)

# # 검색창 클릭
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]').click()

# # 날짜 클릭
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()

# WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table'))

# # 입실날짜
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
# # 퇴실날짜
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
# # 확인버튼
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()

# # 글자입력창 선택
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
# elem.click()
# # 글자입력
# elem.send_keys("강릉 호텔")
# elem.send_keys(Keys.ENTER)

# # 자동실행시 로딩대기
# # 화면의 호텔검색내용이 뜰때까지 대기, 최대30초까지 대기
# WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# # 화면을 스크롤해서 내리기 반복
# # excute_script() : 자바스크립트 실행함수
# prev_height = browser.execute_script("return document.body.scrollHeight")

# while True:
#   browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   time.sleep(1)
#   # 페이지가 로딩되면서 길어진 길이를 다시 가져옴.
#   curr_height = browser.execute_script("return document.body.scrollHeight")
#   # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
#   if prev_height == curr_height:
#     break
#   # 더 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
#   prev_height = curr_height

# print("스크롤 내리기 완료")

# soup = BeautifulSoup(browser.page_source,"lxml")

# browser.close()

# # html저장하기
# with open("c1024/yanolja.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())

# 파일불러와서 soup으로 파싱
soup = ''
with open("c1024/yanolja.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")

# 평점이 4.8이상, 금액:17만원 이하 검색해서 출력하시오.
# 1.
# 호텔명 :
# 평점 :
# 금액 :
# ------------------
# 2.
# 호텔명 :

data = soup.select_one('div.PlaceListBody_listContainer__2qFG1')

hotels = data.select("div.PlaceListItemText_container__fUIgA")
print("개수 :",len(hotels))
search_num = 0
fail_num = 0
search_list = []

for idx,hotel in enumerate(hotels):
  name = hotel.select_one("strong.PlaceListTitle_text__2511B").text.strip()
  rank = hotel.select_one("span.PlaceListScore_rating__3Glxf")
  if rank is not None: rank = float(rank.text.strip())
  price_place = hotel.select_one("div.PlacePriceInfoV2_bottomInfo__2h62q")
  price = price_place.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK")
  if price is not None: price = int(price.text.replace(",",""))

  if rank is None or price is None or rank < 4.8 or price > 170000:
    fail_num += 1
    continue

  h = {}
  h["idx"] = idx+1
  h["name"] = name
  h["rank"] = rank if rank is not None else "없음"
  h["price"] = price if price is not None else "예약마감"
  search_list.append(h)
  search_num += 1

print("맞는 개수 :",search_num)
print("맞지않는 개수 :",fail_num)

search_list.sort(key=lambda x:x["rank"], reverse=True)

for h in search_list:
  print(f"{h["idx"]}.")
  print("호텔명 :",h["name"])
  print("평점 :",h["rank"])
  print("금액 :",h["price"])
  print("-"*50)
