students = []
no = 1

#
# 학생성적 입력부분을 구현하시오.
# dict타입으로 입력을 할것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.

while True:
  print("[ 학생성적프로그램 ]")
  print("1.학생성적입력")
  print("2.학생성적출력")
  print("3.학생성적수정")
  print("4.학생성적검색")
  print("5.학생성적삭제")
  print("6.등수처리")
  print("0.종료")

  choice = input("번호를 입력하세요 >> ")

  if choice == '1':
    print("[ 학생성적입력 ]")
    name = input("학생 이름을 입력하세요.(0.상위)>> ")
    if name == "0":
      break
    kor = int(input("국어성적을 입력하세요.>> "))
    eng = int(input("영어성적을 입력하세요.>> "))
    math = int(input("수학성적을 입력하세요.>> "))
    total = kor+eng+math
    avg = total/3
    students.append({'no':no, "name":name, "kor":kor, "eng": eng, "math": math, "total": total, "avg":avg, "rank": 0})
  elif choice == '2':
    print("[ 학생성적출력 ]")
  elif choice == '3':
    print("[ 학생성적수정 ]")
  elif choice == '4':
    print("[ 학생성적검색 ]")
  elif choice == '5':
    print("[ 학생성적삭제 ]")
  elif choice == '6':
    print("[ 등수처리 ]")
  elif choice == '0':
    print("[ 종료 ]")
  else:
    print("잘못된 명령어")