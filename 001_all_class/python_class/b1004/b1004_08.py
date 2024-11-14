students = []
no = 1
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>>")

  if choice == '1':
    while True:
      print("[ 학생성적 입력 ]")
      name = input("이름을 입력하세요.(상위이동:0)")
      if name == '0':
        print("메뉴화면으로 이동합니다.")
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      print(f"번호:{no},이름:{name},국어:{kor},영어:{eng},수학:{math},합계:{total},평균:{avg:.2f}")

      s = [no,name,kor,eng,math,total,avg, rank]
      students.append(s)
      no+=1
  elif choice == '2':
    print("[ 학생성적 출력 ]")

    # 출력
    s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*60)

    # 학생성적출력
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    print()
  elif choice == '3':
    print("[ 학생성적 수정 ]")
    print()
  elif choice == '0':
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break
  

# 이름,국어,영어,수학 -> 번호,이름,국어,영어,수학,합계,평균
# 이름 0입력하면 프로그램 종료합니다. 출력

# no = 1
# while True: # 홍길동,유관순
#   name = input("이름을 입력하세요.(종료:0)")
#   if name == '0':
#     print("프로그램을 종료합니다.")
#     break
#   kor = int(input("국어점수를 입력하세요."))
#   eng = int(input("영어점수를 입력하세요."))
#   math = int(input("수학점수를 입력하세요."))
#   total = kor+eng+math
#   avg = total/3
#   print(f"번호:{no},이름:{name},국어:{kor},영어:{eng},수학:{math},합계:{total},평균:{avg:.2f}")

#   s = [no,name,kor,eng,math,total,avg]
#   students.append(s)
#   no+=1

# print(students)