import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

cont = soup.find("div",{"id":"conts"})
hot = cont.find("div",{"class":"hot_issue"})
li = hot.find("li", {"class":"issue_list04"})
dl = li.find_all("dl")

print(dl[0].find("img")["src"])

with open("c1021/2.jpg","wb") as f:
  req_img = requests.get(dl[0].find("img")["src"])
  f.write(req_img.content)