# import S_func
from S_func import *

# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
choice = 0 # 전역변수
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경

# -------------------- 
# 학생성적프로그램
while True:
  choice = title_program()        # 메뉴출력함수 호출
  if choice == "1":
    stuNo = stu_input(stuNo,students)      # 학생성적입력함수 호출
  elif choice == "2":
    stu_output(students)
  #-----------------------
  # 3,4,5,6
  elif choice == "3":
    stu_update(students)
  elif choice == "4":
    stu_select(students)
  elif choice == "5":
    stu_delete(students)
  elif choice == "6":
    stu_rank(students)
  #-----------------------
  elif choice == "7":
    while True:
      print("[ 학생성적 정렬 ]")
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
      elif choice == "0":
        print("이전페이지로 이동합니다.")
        break
      print("정렬이 완료되었습니다.")
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break
# 학생성적 입력부분을 구현하시오.
# dict타입으로 입력을 할것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.