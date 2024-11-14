# members리스트 딕셔너리 저장
members = []

# 파일불러오기
m_title = ['id','pw','name','nicName','address','money']
m_tab = [15, 6, 15, 15, 25, 10]

f = open('b1017/member.csv','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  # c리스트 저장
  c = list(map(lambda x:int(x) if x.isdigit() else x, line.strip().split(',')))
  members.append(dict(zip(m_title,c)))

f.close()

# 아이디 검색
# member 리스트에서 입력한 문자로 검색한 데이터를 모두 출력하시오.
# a가 들어가 있는 아이디를 출력

# 데이터 저장
def save_data(members):
  f = open('b1017/members.csv','w',encoding='utf-8')

  for m in members:
    f.write(','.join(list(m.values())))

  f.close()
  print("저장되었습니다.")

# members리스트 출력
def print_members(members):
  if len(members):
    print("   ",end='|')
    for i,k in enumerate(m_title):
      print(f"{k:^{m_tab[i]}}",end='|')
    print()
    print("-"*100)

    for i,m in enumerate(members):
      print(f"{i+1:2} ",end='|')
      for idx,j in enumerate(m.values()):
        print(f"{j:^{m_tab[idx]}}",end='|')
      print()

# 회원 검색
def find_name(user_name):
  mArr = []
  flag = 0
  for m in members:
    if m['name'].find(user_name) != -1:
      mArr.append(m)
      flag = 1
  
  if flag == 0:
    print(f"\"{user_name}\" 검색 결과가 없습니다.")
  else:
    print(f"\"{user_name}\" {len(mArr)}개 검색 결과입니다.")
    print_members(mArr)

# 회원등록
def add_user(members):
  id = input("ID를 입력하세요.>> ")
  
  for m in members:
    if m['id'] == id:
      print(f"{id}는 동일한 아이디가 있습니다. 다시 입력하세요.")
      break
  else:
    print(f"{id}는(은) 사용가능합니다.")
  
  pw = input("PW를 입력하세요.>> ")
  name = input("이름을 입력하세요.>> ")
  nicName = input("닉네임을 입력하세요.>> ")
  address = input("주소를 입력하세요.>> ")
  money = int(input("충전금액을 입력하세요.>> "))
  members.append(dict(zip(m_title,[id,pw,name,nicName,address,money])))
  print(f"{id}님 회원가입이 완료되었습니다.")



# while True:

#   find_name(input("찾을 아이디를 입력해주세요.>> "))