import requests
from bs4 import BeautifulSoup

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,"lxml")
blist = soup.find("div",{"id":"bestPrdList"}).find("ul",{"class":"cfix"})
bitems = blist.find_all("li")

for i,b in enumerate(bitems):
  pname = b.find("div",{"class":"pname"})
  normal_price = pname.find("s",{"class":"normal_price"})
  sale_price = pname.find("strong",{"class":"sale_price"})
  print(f"{i+1}. {pname.find("p").text}")
  print(normal_price.text + " -> " + sale_price.text + "원" if normal_price else sale_price.text + "원")
