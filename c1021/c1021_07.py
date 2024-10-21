import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,"lxml")

newsList = soup.find("div", {"class":"rankingnews_box_wrap"}).find("div",{"class":"rankingnews_box"})
ranks = newsList.find("ul",{"class":"rankingnews_list"})

print("타이틀 :", newsList.find("strong", {"class":"rankingnews_name"}).text)

tlists = ranks.find_all("li")

for i,t in enumerate(tlists):
  print(f"{i+1}. {t.find("a").text}")
