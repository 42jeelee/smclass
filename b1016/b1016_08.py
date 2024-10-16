# sm shop
from datetime import datetime

products = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]
p_title = ["번호","아이디","이름","상품코드","상품명","가격","구매일자"]

members = []
m_keys = ['id','pw','name','nicName','address','money']

cart = []
c_keys = ['cno','id','name','pCode','pName','price','date']

session_info = {}

def load_data():
  f = open('b1016/member.txt','r',encoding='utf-8')

  while True:
    line = f.readline()
    if not line: break
    m = line.strip().split(",")
    m[5] = int(m[5])
    members.append(dict(zip(m_keys,m)))
  f.close()

  f = open('b1016/cart.txt','r',encoding='utf-8')

  while True:
    line = f.readline()
    if not line: break
    c = line.strip().split(',')
    c[0], c[5] = int(c[0]), int(c[5])
    cart.append(dict(zip(c_keys,c)))
  f.close()

def save_data(fileName, obj):
  f = open(fileName,'w',encoding='utf-8')

  for m in obj:
    f.write(",".join([str(i) for i in m.values()])+'\n')
  
  f.close()

def print_data(obj):
  
  if len(obj):
    print(end='\t')
    for o in obj[0].keys():
      print(o,end='\t')
    print()
    print("-"*80)

    for i,o in enumerate(obj):
      print(i,end='\t')
      for j in o.values():
        if type(j) == int: print(f"{j:,}",end='\t')
        else: print(j,end='\t')
      print()
  else:
    print("[ 빈 데이터 ]")

def login(members):
  while True:
    print("[ 로그인 화면 ]")
    input_id = input("아이디를 입력하세요.(0.종료)>> ")
    if input_id == "0":
      return None
    input_pw = input("패스워드를 입력하세요.>> ")

    for m in members:
      if input_id == m['id'] and input_pw == m['pw']:
        print("SM SHOP에 온 것을 환영합니다.!")
        return m
    print("아이디 또는 패스워드가 일치하지 않습니다.!")

def buy(choice, cart, session_info):
  print(f"'{products[choice-1]['pName']}'을(를) 구매하셨습니다.")
  now = datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  c = {'cno': len(cart),'id': session_info['id'],'name': session_info['name'],'pCode': products[choice-1]['pCode'],'pName':products[choice-1]['pName'],'price':products[choice-1]['price'],'date':today}

  session_info['money'] -= products[choice-1]['price']
  cart.append(c)

def showmethemoney():
  input_money = int(input("얼마를 충전하시겠습니까?>> "))
  session_info['money'] += input_money
  print("충전이 완료되었습니다.")

load_data()
session_info = login(members)

if session_info != None:
  print("로그인되었습니다.")
  while True:
    print("          [ SM-SHOP ]")
    print(f"                              닉네임: {session_info['nicName']}님")
    print(f"                                금액: {session_info['money']:,} 원")
    print("1. 삼성TV - 2,000,000")
    print("2. LG냉장고 - 3,000,000")
    print("3. 하만카돈스피커 - 500,000")
    print("4. 세탁기 - 1,000,000")
    print("7. 내용저장")
    print("8. 구매내역")
    print("9. 금액충전")
    print("0. 프로그램 종료")
    choice = int(input("구매하려는 상품번호를 입력하세요.(0.종료)>> "))
    if 1 <= choice <= 4:
      buy(choice, cart, session_info)
    elif choice == 7:
      save_data('b1016/member.txt', members)
      save_data('b1016/cart.txt', cart)
      print("내용이 저장되었습니다.")
    elif choice == 8:
      print_data(cart)
    elif choice == 9:
      showmethemoney()
    elif choice == 0:
      break

print("프로그램을 종료합니다.")