import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

f = open("c1022/melon.txt","w",encoding="UTF-8")

# 순위, 사진링크주소, 제목, 가수명
data = soup.select_one("#frm > div > table > tbody")
trs = data.select("tr")

st_lists = []
for tr in trs:
  st_list = []
  tds = tr.select("td")

  print("순위 :",tds[1].text)
  print("사진 url :",tds[3].select_one("img").get("src"))
  print("제목 :",tds[5].select_one(".ellipsis.rank01").text.strip())
  print("가수명 :",tds[5].select_one(".ellipsis.rank02>a").text.strip())

  st_list.append(tds[1].text)
  st_list.append(tds[3].select_one("img").get("src"))

  with open(f"c1022/images/{tds[5].select_one(".ellipsis.rank01").text.strip().replace("?","")}.jpg","wb") as f2:
    f2.write(requests.get(tds[3].select_one("img").get("src")).content)

  st_list.append(tds[5].select_one(".ellipsis.rank01").text.strip())
  st_list.append(tds[5].select_one(".ellipsis.rank02>a").text.strip())

  f.write(','.join(st_list)+'\n')
  st_lists.append(st_list)

f.close()
