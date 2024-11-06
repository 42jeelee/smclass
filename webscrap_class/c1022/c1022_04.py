import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("#contentarea div.box_type_l")

theads = data.select("tr.type1>th")

for th in theads:
  print(th.text,end="\t")
print()
print("-"*60)

tdatas = data.select("tr:not(.type1)")

for td in tdatas[1].select("td"):
  print("|" + td.text.strip() + "|")

# for tdata in tdatas:
#   tds = tdata.select("td")

#   for td in tds:
#     print(td.text.strip(),end="\t")
#   print()