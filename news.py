import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import datetime

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div")

items = data.select("div.rankingnews_box")

fmsg = f"언론사 개수 : {len(items)}\n"
# print("개수 :",len(items))
for item in items:
  name = item.select_one("strong.rankingnews_name").text
  ul = item.select_one("ul.rankingnews_list")
  lis = ul.select("li")
  # print(f"[ {name} ]")
  # print(f"개수 : {len(lis)}")
  fmsg += f"[ {name} ]\n뉴스 개수 : {len(lis)}\n"
  for idx,li in enumerate(lis):
    content = li.select_one("div.list_content>a").text
    # print(content)
    fmsg += f"{idx+1}. {content}\n"
  fmsg += "-"*60 + "\n"

# print(fmsg)

smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = "kaimahi@naver.com"
pw = "ZV18TYVWT39V"
recvEmail = "jeelee553@gmail.com"

today = datetime.datetime.now()
title = f"{today.__format__("%Y-%m-%d")} 네이버 랭킹뉴스"

msg = MIMEText(fmsg)
msg["Subject"] = title
msg["From"] = sendEmail
msg["To"] = recvEmail

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.quit()

# 메일발송 완료
print("메일을 발송했습니다.")