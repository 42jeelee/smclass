import datetime
import os
members = []
m_title = ['id','pw','name','nicName','address','money']
#### member.csv파일 불러오기
f = open('b1017/member.csv',"r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  # c리스트 저장
  c = line.strip().split(",")
  c[5] = int(c[5])  # money
  # members리스트에 딕셔너리 저장
  members.append(dict(zip(m_title,c)))
f.close()
#-----------------------------
# cart.txt파일 읽기, member딕셔너리 저장
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]
# isfile : 파일인지확인, isdir : 디렉토리인지 확인, exists : 파일이 존재하는지 확인
if os.path.exists("b1017/cart.csv"):
  f = open('b1017/cart.csv','r',encoding='utf-8')
  while True:
    line = f.readline()
    if not line: break
    c = line.strip().split(",")
    c[0] = int(c[0])
    c[5] = int(c[5])
    cart.append(dict(zip(c_keys,c)))
  f.close()
#-----------------------------------------
# 파일 저장해서 불러오기 -> 09
product = []
p_keys = ["pno","pCode","pName","price","color"]
if os.path.exists("b1017/products.csv"):
  f = open('b1017/products.csv','r',encoding='utf-8')
  while True:
    line = f.readline()
    if not line: break
    c = line.strip().split(",")
    c[0] = int(c[0])
    c[3] = int(c[3])
    cart.append(dict(zip(p_keys,c)))
  f.close()
session_info = {}
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]

def login():
  global session_info
  input_id = input("아이디를 입력하세요.>> ")
  input_pw = input("패스워드를 입력하세요.>> ")
  
  for m in members:
    if input_id == m['id'] and input_pw == m['pw']:
      session_info = m
      break
  else:
    print("아이디 또는 패스워드가 일치하지 않습니다.")

def register():
  id = input("아이디를 입력하세요.>> ")
  pw = input("패스워드를 입력하세요.>> ")
  name = input("이름을 입력하세요.>> ")
  nicName = input("닉네임을 입력하세요.>> ")
  address = input("주소를 입력하세요.>> ")
  money = input("가지고 있는 금액을 입력하세요.>> ")

  if not money.isdigit():
    print("금액은 숫자여야 합니다.")
    return

  members.append(dict(zip(m_title,[id,pw,name,nicName,address,money])))
  print("정상적으로 회원가입이 되었습니다.")

def save_data():
  f = open('b1017/members.csv','w',encoding='UTF-8')

  for m in members:
    f.write(",".join([str(i) for i in m.values()]) + '\n')

  f.close()

  f = open('b1017/cart.csv','a',encoding='UTF-8')

  for c in cart:
    f.write(','.join([str(i) for i in c.values()]) + '\n')

  f.close()

def buy(choice):
  global session_info
  print(f"{product[choice-1]} 상품을 구매합니다.")
  
#####  프로그램 시작  #####
while True:
  print("[ 메인화면 ]")
  print("1. 로그인")
  print("2. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.>>")
  if choice == "1":
    login()
  elif choice == "2":
    register()
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break
  # 프로그램을 구현하시오.

  if session_info != {}:
    print("로그인 되었습니다.")
    while True:
      print("           [ SM-SHOP ]")
      print(f"                       닉네임:{session_info['nicName']}님")
      print(f"                       금액 :{session_info['money']:,} 원")
      print("1. 삼성TV - 2,000,000")
      print("2. LG냉장고 - 3,000,000")
      print("3. 하만카돈스피커 - 500,000")
      print("4. 세탁기 - 1,000,000")
      print("7. 내용저장")
      print("8. 구매내역 ")
      print("9. 금액충전 ")
      print("0. 로그아웃")
      choice = int(input("구매하려는 상품번호를 입력하세요.>> "))
      # 프로그램 구현
      if 1 <= choice <= 4:
        pass
      elif choice == 7:
        save_data()
      elif choice == 8:
        pass
      elif choice == 9:
        pass
      elif choice == 0:
        print("로그아웃합니다.")
        break