import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
sum = 0
# print(soup.select_one("h3.h_popular>span"))

# 기준점
data = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular")

# 인기검색종목
print(data.select_one("span").text)
# 1,2,3,4,5위
pops = data.select("tbody>tr")
print("개수 :",len(pops))

for pop in pops:
  sum += int(pop.select_one("td").text.replace(",",""))
  print(f"{pop.select_one("th>a").text} : {pop.select_one("td").text} ( {pop.select_one("td:last-child>span").text.strip()} {pop.select_one("td:last-child>em>span").text} )")

print("합계 :",sum)