s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 메뉴출력함수 시작
def title_program():
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
  return choice
# --------------------
# 학생성적입력함수 시작 - 일반변수 변경
def stu_input(stuNo,students):
  while True:
      print("[ 학생성적 입력 ]")
      # 학생성적 직접 입력
      no = stuNo + 1  # 리스트 - 학생수
      name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>")
      if name == "0":
        print("성적입력을 취소합니다.")
        print()
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      ss = { "no":no,"name":name,"kor":kor,"eng":eng,
             "math":math,"total":total,"avg":avg,"rank":rank }
      students.append(ss)
      stuNo += 1  # 학생수 1증가
      print(f"{name} 학생성적이 저장되었습니다.!")
      print()
  return stuNo
# --------------------
# 학생성적출력 함수선언
def stu_output(students):
  print("[ 학생성적 출력 ]")
  print()

  # 상단출력
  for st in s_title:
    print(st,end="\t")
  print(); print("-"*60)

  # 학생성적출력
  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()
# --------------------
# 학생성적수정 함수선언
def stu_update(students):
  print("[ 학생성적수정 ]")
  name = input("찾고자 하는 학생의 이름을 입력하세요.")
  chk = 0
  for s in students:
    if s['name'] == name:
      # 학생성적 수정
      print(f"{name} 학생을 찾았습니다.")
      print()
      print("[ 수정 과목 선택 ]")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      choice = input("원하는 번호를 입력하세요.>> ")
      if choice == "1":
        print("이전 국어점수 : {}".format(s['kor']))
        s['kor'] = int(input("변경 국어점수 : "))
      elif choice == "2":
        print("이전 영어점수 : {}".format(s['eng']))
        s['eng'] = int(input("변경 영어점수 : "))
      elif choice == "3":
        print("이전 수학점수 : {}".format(s['math']))
        s['math'] = int(input("변경 수학점수 : "))
      s['total'] = s['kor']+s['eng']+s['math']  # 합계
      s['avg'] = s['total']/3          # 평균
      print(f"{name} 학생 성적이 수정되었습니다.")
      print()
      # 학생출력
      # 상단타이틀 출력
      for title in s_title:
        print(f"{title}\t",end="")
      print()
      print("-"*60)
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
      print()
      chk = 1
  # 모든 학생 비교가 끝난 후, chk 확인
  if chk == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")
  print()

# --------------------
# 학생성적검색 함수선언
def stu_select(students):
  while True:
    flag = 0
    print("[ 학생성적검색 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요.(0.이전화면 이동)")
    if name == "0":
      break
    sArr = []
    for idx,s in enumerate(students):
      if s['name'].find(name) != -1:
        sArr.append(s)
        flag = 1

    if flag == 0:
      print("찾는 학생이 없습니다.")
    else:
      print(f"{name} 이름으로 {len(sArr)}명 검색되었습니다.")
      stu_output(sArr)
# --------------------
# 학생성적삭제함수 선언
def stu_delete(students):
  print("[ 학생성적 삭제 ]")
  name = input("찾고자 하는 학생의 이름을 입력하세요.")
  flag = 0
  sArr = []
  for idx,s in enumerate(students):
    flag = 1
    if s['name'] == name:
      print(f"{name} 학생성적을 삭제하시겠습니까?( 삭제시 복구불가 )")
      print("1.삭제 2.취소")
      choice = input("원하는 번호를 입력하세요.>> ")
      if choice == "1":
        sArr.append(s)
        del students[idx]
        print(f"{name} 학생성적이 삭제되었습니다.")
        break
      else:
        print("학생성적 삭제가 취소되었습니다.")
        break

  # 모든 학생 비교가 끝난 후, flag 확인
  if flag == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")

  stu_output(sArr)

# --------------------
# 6. 학생성적프로그램
def stu_rank(students):
  print("[ 등수처리 ]")
  for s in students:
    count = 1
    for st in students:
      if s['total'] < st['total']:
        count += 1
    s['rank'] = count # 등수입력
  print("등수처리가 완료되었습니다.")
  print()
