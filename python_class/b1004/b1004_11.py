students = []
no = 1
s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]

while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료) >> ")

  if choice == '1':
    while True:
      print("[ 학생성적 입력 ]")
      name = input("이름을 입력하세요. (상위:0)")
      if name == '0':
        break
      kor = int(input("국어점수를 입력하세요. "))
      eng = int(input("영어점수를 입력하세요. "))
      math = int(input("수학점수를 입력하세요. "))
      total = kor+eng+math
      avg = total/3
      students.append([no,name,kor,eng,math,total,avg,0])
      print("저장되었습니다.")

      no += 1

  elif choice == '2':
    for t in s_title:
      print(t,end='\t')
    print()
    print("-"*60)

    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    if len(students) == 0:
      print("< 입력된 학생이 없습니다. >")
    print()
  elif choice == '3':
    name = input("찾고자 하는 학생의 이름을 입력하세요. ")
    count = 0
    for s in students:
      if s[1] == name:
        count += 1
        print(f"{name} 학생을 찾았습니다.")
        print("[ 과목선택 ]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("원하는 번호를 입력하세요.(그 외.종료) >> ")
        if choice == '1':
          print("현재 국어성적 :",s[2])
          s[2] = int(input("변경 국어점수 입력 : "))
        elif choice == '2':
          print("현재 영어성적 :",s[3])
          s[3] = int(input("변경 영어점수 입력 : "))
        elif choice == '3':
          print("현재 수학성적 :",s[4])
          s[4] = int(input("변경 수학점수 입력 : "))
        if  choice == '1' or  choice == '2' or  choice == '3':
          s[5] = s[2]+s[3]+s[4]
          s[6] = s[5]/3
          print("변경이 완료되었습니다.")
    if count == 0:
      print("찾고자 하는 학생의 이름이 없습니다.")
    print()
  elif choice == '4':
    name = input("찾고자 하는 학생의 이름을 입력하세요. ")
    count = 0
    for s in students:
      if s[1] == name:
        count += 1
        print(f"{name} 학생을 찾았습니다.")

        for t in s_title:
          print(t,end='\t')
        print()
        print("-"*60)

        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    if count == 0:
      print("찾고자 하는 학생의 이름이 없습니다.")
    print()
  elif choice == '5':
    name = input("찾고자 하는 학생의 이름을 입력하세요. ")
    count = 0
    for idx,s in enumerate(students):
      if s[1] == name:
        count += 1
        print(f"{name} 학생을 찾았습니다.")
        del students[idx]
        print(f"{name} 학생성적을 삭제하였습니다.")
    if count == 0:
      print("찾고자 하는 학생의 이름이 없습니다.")
    print()
  elif choice == '6':
    pass
  elif choice == '0':
    print("프로그램을 종료합니다.")
    break