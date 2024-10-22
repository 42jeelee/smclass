import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# print(res.text)

soup = BeautifulSoup(res.text,"lxml")
# print(soup.find("h2",{"class":"rankingnews_tit"}))
# print(soup.select_one("h2.rankingnews_tit").text)
# print(soup.select_one("div#header"))

# select_one 사용
data = soup.select_one("div.rankingnews_box_wrap")
news = data.select_one("div.rankingnews_box")
print("언론사 이름 :",news.select_one("strong.rankingnews_name").text)
news_lists = news.select("ul.rankingnews_list>li")
print("개수 :",len(news_lists))

for idx,news_list in enumerate(news_lists):
  print(f"{idx+1} : {news_list.select_one("div.list_content>a").text}")
