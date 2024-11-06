from bs4 import BeautifulSoup

# flight.html 금액이 70000원 미만 항공권을 출력하시오.
# 김포-제주 70000원이하 항공권 개수 : 15개
# 제주-김포 70000원이하 항공권 개수 : 30개

f = open("c1023/flight.html","r",encoding="UTF-8")
soup = BeautifulSoup(f,"lxml")
f.close()

data = soup.select_one(".domestic_results__gp5WB")

tickets = data.select(".domestic_Flight__8bR_b")

print("[ 김포-제주 항공권 ]")
for ticket in tickets:
  fname = ticket.select_one(".airline_name__0Tw5w").text.strip()
  times = ticket.select(".route_airport__tBD9o")
  price = int(ticket.select_one(".domestic_price__SAqlB>i").text.strip().replace(",",""))

  if price > 70000: continue

  print("항공사 :",fname)
  print("출발시간 :",times[0].text.strip().replace("\n",""))
  print("도착시간 :",times[1].text.strip().replace("\n",""))
  print("등급 :",ticket.select_one(".domestic_type__izlcp").text.strip())
  print("가격 :",price)
  print("-"*50)