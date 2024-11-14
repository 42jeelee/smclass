RED_COLOR = "\033[0;31m"
GREEN_COLOR = "\033[0;32m"
YELLOW_COLOR = "\033[0;33m"
BLUE_COLOR = "\033[0;34m"
BOLD_COLOR = "\033[1m"
CLEAR_ANSI = "\033[0m"
CLEAR_CONSOLE = "\033[2J\033[H"

students = []
no = 1
chk = 0

head_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]

while True:
  print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적 프로그램 ]"+CLEAR_ANSI)
  print("-"*60)
  print("1.학생성적입력")
  print("2.학생성적출력")
  print("3.학생성적수정")
  print("4.학생성적검색")
  print("5.학생성적삭제")
  print("6.등수처리")
  print("0.프로그램 종료")
  print("-"*60)
  choice = input(BOLD_COLOR+"원하는 번호를 입력하세요.(0.종료)>> "+CLEAR_ANSI)

  if choice == "1":
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적입력 ]"+CLEAR_ANSI)
    name = input("학생 이름을 입력하세요.(0.상위)>> ")
    if name == "0":
      break
    kor = int(input("국어성적을 입력하세요.>> "))
    eng = int(input("영어성적을 입력하세요.>> "))
    math = int(input("수학성적을 입력하세요.>> "))
    total = kor+eng+math
    avg = total/3
    students.append([no,name,kor,eng,math,total,avg,0])
    no += 1
    input(YELLOW_COLOR+"\n학생성적이 저장되었습니다.\n"+CLEAR_ANSI)
  elif choice == "2":
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적출력 ]"+CLEAR_ANSI)
    
    print(GREEN_COLOR)
    for h in head_title:
      print(h,end='\t')
    print("\n"+CLEAR_ANSI,"-"*80,sep='')

    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    print("-"*80)
    input()
  elif choice == "3":
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적수정 ]"+CLEAR_ANSI)
    name = input("수정하고자 하는 학생이름을 입력하세요.>> ")
    for s in students:
      if name == s[1]:
        chk = 1
        print(YELLOW_COLOR + f"{name} 학생을 찾았습니다."+CLEAR_ANSI)

        print(BOLD_COLOR+"[성적 수정]"+CLEAR_ANSI)
        print("-"*30)
        print("1.국어")
        print("2.영어")
        print("3.수학")
        print("-"*30)
        choice = input(BOLD_COLOR+"수정할 성적을 입력하세요.>> "+CLEAR_ANSI)
        if choice == "1":
          print("수정 전 국어성적 :", s[2])
          s[2] = int(input("국어성적을 입력하세요.>> "))
        elif choice == "2":
          print("수정 전 영어성적 :", s[3])
          s[3] = int(input("영어성적을 입력하세요.>> "))
        elif choice == "3":
          print("수정 전 수학성적 :", s[4])
          s[4] = int(input("수학성적을 입력하세요.>> "))
        else:
          print(RED_COLOR+"선택지에 존재하지 않습니다.."+CLEAR_ANSI)
          break
        s[5] = s[2]+s[3]+s[4]
        s[6] = s[5]/3
        print(YELLOW_COLOR+"수정이 완료되었습니다."+CLEAR_ANSI)
        break
    if chk == 0:
      print(RED_COLOR + f"{name} 학생이 없습니다."+CLEAR_ANSI)
    chk = 0
    input()
  elif choice == "4":
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적검색 ]"+CLEAR_ANSI)
    name = input("찾고자 하는 학생이름을 입력하세요.>> ")
    for s in students:
      if name == s[1]:
        chk = 1
        print(YELLOW_COLOR + f"{name} 학생을 찾았습니다."+CLEAR_ANSI)

        print(GREEN_COLOR)
        for h in head_title:
          print(h,end='\t')
        print("\n"+CLEAR_ANSI,"-"*80,sep='')

        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
        print("-"*80)
    if chk == 0:
      print(RED_COLOR + f"{name} 학생이 없습니다."+CLEAR_ANSI)
    chk = 0
    input()
  elif choice == "5":
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 학생성적삭제 ]"+CLEAR_ANSI)
    name = input(BOLD_COLOR+"삭제하고자 하는 학생이름을 입력하세요.>> "+CLEAR_ANSI)
    for idx,s in enumerate(students):
      if name == s[1]:
        chk = 1
        print(YELLOW_COLOR + f"{name} 학생을 찾았습니다."+CLEAR_ANSI)

        choice = input(BOLD_COLOR+"정말로 삭제하시겠습니까?(Y/N)>> "+CLEAR_ANSI)
        if choice == "Y" or choice == "y":
          del students[idx]
          print(YELLOW_COLOR+"삭제되었습니다."+CLEAR_ANSI)
    if chk == 0:
      print(RED_COLOR + f"{name} 학생이 없습니다."+CLEAR_ANSI)
    chk = 0
    input()
  elif choice == "6":
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 등수처리 ]"+CLEAR_ANSI)
    for i in students:
      rank = 1
      for j in students:
        if i[5] < j[5]:
          rank += 1
      i[7] = rank
    input(YELLOW_COLOR+"등수처리가 완료되었습니다.\n"+CLEAR_ANSI)
  elif choice == "0":
    print(CLEAR_CONSOLE+BLUE_COLOR+BOLD_COLOR+"[ 프로그램 종료 ]"+CLEAR_ANSI)
    print(RED_COLOR+"프로그램을 종료합니다."+CLEAR_ANSI)
    break
  else:
    input(YELLOW_COLOR+"선택지에 존재하지 않습니다.."+CLEAR_ANSI)