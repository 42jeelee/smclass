# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
k_title = ["no","name","kor","eng","math","total","avg","rank"]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)+1  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# ----------------
# 학생성적입력 함수선언
def stu_input(students):
  global stuNo
  while True:
    print("[ 학생성적입력 ]")
    name = input("이름을 입력하세요.(0.이전화면)>> ")
    if name == "0":
      print("이전화면으로 이동합니다.")
      break
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    total = kor+eng+math
    avg = total/3
    students.append({"no": stuNo, "name": name, "kor": kor, "eng": eng, "math": math, "total": total, "avg": avg, "rank": 0 })
    stuNo += 1
    print(f"{stuNo}번째 학생 저장이 완료되었습니다.")

# ----------------
# 학생성적출력 함수선언
def stu_output(students):
  print("[ 학생성적출력 ]")

  for t in s_title:
    print(t,end='\t')
  print()
  print("-"*60)

  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()

# ----------------
# 학생성적수정 함수선언
def stu_update(students):
  print("[ 학생성적수정 ]")
  flag = 0
  name = input("수정할 학생의 이름을 입력하세요.>> ")
  for s in students:
    if s['name'] == name:
      flag = 1
      print(f"{name} 학생을 찾았습니다.")
      print("[ 수정 과목 입력 ]")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      choice = int(input("원하는 번호를 입력하세요."))+1

      print(f"이전 {s_title[choice]}점수 : {s[k_title[choice]]}")
      s[k_title[choice]] = int(input(f"변경 {s[s_title[choice]]}점수>> "))

      s['total'] = s['kor']+s['eng']+s['math']
      s['avg'] = s['total']/3

      print(f"{name} 학생성적 수정이 완료되었습니다.")

      stu_output([s])
      break
  if flag == 0:
    print(f"{name} 학생을 찾을 수 없습니다.")
# ----------------
# 학생성적검색 함수선언
def stu_select(students):
  print("[ 학생성적검색 ]")
  flag = 0
  name = input("찾고자 하는 학생을 입력하세요.>> ")
  for s in students:
    if name == s['name']:
      flag = 1
      print(f"{name} 학생을 찾았습니다.")

      stu_output([s])
      break
  if flag == 0:
    print(f"{name} 학생을 찾을 수 없습니다.")
# ----------------
# 학생성적삭제 함수선언
def stu_delete(students):
  print("[ 학생성적삭제 ]")
  flag = 0
  name = input("삭제하고자 하는 학생을 입력하세요.>> ")
  for i,s in enumerate(students):
    if name == s['name']:
      flag = 1
      print(f"{name} 학생을 삭제하시겠습니까?(삭제시 되돌릴 수 없습니다.)")
      print("1.삭제 2.취소")
      choice = input("원하는 번호를 입력하세요.")
      if choice == "1":
        del students[i]
        print("삭제되었습니다.")
      break
  if flag == 0:
    print(f"{name} 학생을 찾지 못했습니다.")

# ----------------
# 등수처리 함수선언
def stu_rank(students):
  print("[ 등수처리 ]")
  for i in students:
    count = 1
    for j in students:
      if i['total'] > j['total']:
        count += 1
    i['rank'] = count
  print("등수처리가 완료되었습니다.")
# ----------------
# 학생성적정렬 함수선언
def stu_order(students):
  while True:
    print("[ 학생성적정렬 ]")
    print("1. 이름 순차정렬")
    print("2. 이름 역순정렬")
    print("3. 합계 순차정렬")
    print("4. 합계 역순정렬")
    print("5. 번호 순차정렬")
    print("0. 이전페이지 이동")
    print("-"*40)
    choice = input("원하는 번호를 입력하세요.>> ")
    if choice == "1":
      students.sort(key=lambda x:x['name'])
    elif choice == "2":
      students.sort(key=lambda x:x['name'],reverse=True)
    elif choice == "3":
      students.sort(key=lambda x:x['total'])
    elif choice == "4":
      students.sort(key=lambda x:x['total'],reverse=True)
    elif choice == "5":
      students.sort(key=lambda x:x['no'])
    elif choice == "0":
      print("이전화면으로 이동합니다.")
      break
    print("정렬이 완료되었습니다.")
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == "1":
    stu_input(students)
  elif choice == "2":
    stu_output(students)
  elif choice == "3":
    stu_update(students)
  elif choice == "4":
    stu_select(students)
  elif choice == "5":
    stu_delete(students)
  elif choice == "6":
    stu_rank(students)
  elif choice == "7":
    stu_order(students)
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break