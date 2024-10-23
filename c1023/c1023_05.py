from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# # 파일 불러와서 저장하기 - i회
# for i in range(5):
#   url = f"https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false&page={i+1}"
#   # Chrome() ()안에 chromedriver.exe 위치 지점을 입력해줘야함.
#   # root에 파일이 저장되어 있으면 입력하지 않아도 됨.
#   browser = webdriver.Chrome()
#   # 이동하려는 주소 입력
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   with open(f"c1023/yeogi{i+1}.html","w",encoding="UTF-8") as f:
#     f.write(soup.prettify())
#   data = soup.select_one("#__next > div > main > section > div.css-1qumol3")

# 평점 9.0이상, 평가수 500이상, 금액:120000 이하
# 파일 5개를 모두 검색해서 출력하시오.
soup = ""

for i in range(5):
  # 파일 불러오기 -BeautifulSoup 으로 파싱
  with open(f"c1023/yeogi{i+1}.html","r",encoding="UTF-8") as f:
    soup = BeautifulSoup(f,'lxml')

  # 제목,평점,평가수,금액,이미지,링크주소
  data = soup.select_one("#__next > div > main > section > div.css-1qumol3")

  print(f"[ {i+1} 페이지 ]")

  sells = data.select("a")
  # 평가 수가 500명 이하 제외
  for idx,sell in enumerate(sells):
    num = int(sell.select_one(".css-oj6onp").text.strip()[:-4].replace(",",""))
    price = sell.select_one(".css-yeouz0>.css-5r5920")
    rating = float(sell.select_one(".css-9ml4lz").text.strip());
    img = sell.select_one(".css-nl3cnv>img")
    link = "https://www.yeogi.com" + sell["href"]
    if img is not None: img = img['src']
    if price is not None: price = int(price.text.replace(",",""))
    if num < 500 or rating < 9.0:
      print(f"{i*20+idx+1}번 제외")
      continue
    print("제목 :",sell.select_one("h3").text.strip())
    print("평점 :",rating)
    print("평가수 :",num)
    print("금액 :",price)
    print("이미지 :",img)
    print("링크 :",link)
    print("-"*50)

# time.sleep(10)

# requests정보 가져오기
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")

# with open("c1023/yeogi1.html","w",encoding="UTF-8") as f:
#   f.write(soup.prettify())

# data = soup.select_one("#__next > div > main > section > div.css-1qumol3")
# print(data)