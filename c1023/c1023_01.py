import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 기준점
data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
print(len(stocks))

# 1.상단타이틀.
st_list = [ st.text for st in stocks[0].select("th") ]
# print(st_list)
# print(len(st_list)) # 상단타이틀 항목 : 12개

# 30개 주식정보를 csv파일로 저장하시오.
with open("c1023/stock.csv","w",encoding="utf-8-sig",newline="") as f:
  writer = csv.writer(f)
  for stock in stocks:
    sto_list = [ sto.text.strip().replace("\t","").replace("\n","") for sto in stock.select("td") ]
    if len(sto_list) == 12:
      writer.writerow(sto_list)


# list생성
# sts = stocks[0].select("th")

# st_list = []
# for st in sts:
#   print(st.text)
#   st_list.append(st.text)
# print(st_list)