students = []
no = 1
s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]

RED_COLOR = "\033[0;31m"
GREEN_COLOR = "\033[0;32m"
YELLOW_COLOR = "\033[0;33m"
BLUE_COLOR = "\033[0;34m"
BOLD_COLOR = "\033[1m"
CLEAR_ANSI = "\033[0m"
CLEAR_CONSOLE = "\033[2J\033[H"

# 학생성적프로그램
while True:
  print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적프로그램 ]"+CLEAR_ANSI)
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("-"*60)
  choice = input(BOLD_COLOR+"원하는 번호를 입력하세요.(0.종료) >> "+CLEAR_ANSI)

  if choice == '1':
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적 입력 ]"+CLEAR_ANSI)
    while True:
      name = input("이름을 입력하세요.(상위:0)")
      if name == '0':
        break
      kor = int(input("국어성적을 입력하세요."))
      eng = int(input("영어성적을 입력하세요."))
      math = int(input("수학성적을 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      students.append([no,name,kor,eng,math,total,avg,rank])
      no += 1
      print(CLEAR_CONSOLE+"입력되었습니다.\n"+CLEAR_ANSI)
  elif choice == '2':
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적 출력 ]"+CLEAR_ANSI)
    for t in s_title:
      print(BOLD_COLOR+t+CLEAR_ANSI,end="\t")
    print()
    print("-"*60)

    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    if len(students) == 0:
      print(RED_COLOR+"< 입력된 학생이 없습니다. >"+CLEAR_ANSI)
    print()
    input(BOLD_COLOR+"< 계속하려면 Enter키를 누르세요.. >"+CLEAR_ANSI)
  elif choice == '3':
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적 수정 ]"+CLEAR_ANSI)
    # 홍길동,유관순,이순신
    # 유관순 학생 성적
    name = input("찾고자 하는 학생이름을 입력하세요.>> ")
    # students에서 검색
    count = 0
    for s in students:
      if s[1] == name:
        count += 1
        print(YELLOW_COLOR+f"{name} 학생을 찾았습니다."+CLEAR_ANSI)
        print("[ 과목선택 ]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input(BOLD_COLOR+"원하는 번호를 입력하세요.(그 외.종료) >> "+CLEAR_ANSI)
        if choice == '1':
          print("현재 국어점수는 :",s[2])
          s[2] = int(input("변경 국어점수 입력 : "))
        elif choice == '2':
          print("현재 영어점수는 :",s[3])
          s[3] = int(input("변경 영어점수 입력 : "))
        elif choice == '3':
          print("현재 수학점수는 :",s[4])
          s[4] = int(input("변경 수학점수 입력 : "))
        if choice == '1' or choice == '2' or choice == '3':
          s[5] = s[2]+s[3]+s[4] # 합계변경
          s[6] = s[5]/3 # 평균변경
          print(YELLOW_COLOR+f"{name} 학생의 성적이 변경되었습니다."+CLEAR_ANSI)
    # 없을 경우
    if count == 0:
      print(RED_COLOR+"수정하고자 하는 학생이름이 없습니다."+CLEAR_ANSI)
    input(BOLD_COLOR+"< 계속하려면 Enter키를 누르세요.. >"+CLEAR_ANSI)
  elif choice == '4':
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적 검색 ]"+CLEAR_ANSI)
    name = input("찾고자 하는 학생이름을 입력하세요.>> ")
    # students에서 검색
    count = 0
    for s in students:
      if s[1] == name:
        count += 1
        print(YELLOW_COLOR+f"{name} 학생을 찾았습니다."+CLEAR_ANSI)
        for t in s_title:
          print(BOLD_COLOR+t+CLEAR_ANSI,end="\t")
        print()

        print("-"*60)
        # 학생성적출력
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        print("-"*60)
        input(BOLD_COLOR+"< 계속하려면 Enter키를 누르세요.. >"+CLEAR_ANSI)
    if count == 0:
      print(RED_COLOR+"찾고자 하는 학생의 이름이 없습니다.."+CLEAR_ANSI)
      input(BOLD_COLOR+"< 계속하려면 Enter키를 누르세요.. >"+CLEAR_ANSI)
  elif choice == '0':
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 프로그램 종료 ]"+CLEAR_ANSI)
    print("프로그램을 종료합니다.")
    break