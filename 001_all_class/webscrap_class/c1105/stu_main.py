# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블 사용해서
# 시퀀스 students_seq 생성
# 김유신, 99, 98, 96, 합계, 평균, 등수, 입력일
### 시작 ###
import stu_func


while True:
  choice = stu_func.print_menu()

  if choice == 1:
    stu_func.input_student()
  elif choice == 2:
    stu_func.output_students()
  elif choice == 3:
    stu_func.output_student()
  elif choice == 4:
    stu_func.sort_students()
  elif choice == 5:
    stu_func.rank_students()
  elif choice == 6:
    stu_func.update_student()
  elif choice == 7:
    print(stu_func.GREEN_COLOR + "프로그램을 종료합니다." + stu_func.CLEAR_ANSI)
    break
  input()