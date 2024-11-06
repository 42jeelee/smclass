# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블 사용해서
# 시퀀스 students_seq 생성
# 김유신, 99, 98, 96, 합계, 평균, 등수, 입력일
### 시작 ###
import oracledb

def connects():
  try: conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
  except Exception as e: print("예외처리 :", e)
  return conn

def select_query_db(sql, values = None):
  conn = connects()
  cursor = conn.cursor()
  if values is not None: cursor.execute(sql, values)
  else: cursor.execute(sql)
  data = cursor.fetchall()
  conn.close()
  return data

def modify_query_db(sql, values):
  conn = connects()
  cursor = conn.cursor()
  cursor.execute(sql, values)
  conn.commit()
  conn.close()
  

def print_menu():
  print("[ 학생성적프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적검색")
  print("4. 종료")
  print("-"*50)
  return input("원하는 번호를 입력하세요.>> ")

def print_students(students):
  COLUMN_TITLE = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']

  for i, t in enumerate(COLUMN_TITLE):
    if i == 1: t = f"{t:15s}"

    print(t, end='\t')
  print()
  print("-"*80)

  for student in students:
    for i, s in enumerate(student):
      if i == 1: s = f"{s:15s}"
      elif i == 6: s = f"{s:.2f}"
      elif i == 8: s = s.strftime("%y-%m-%d")

      print(s, end='\t')
    print()

def input_student():
  print("[ 학생성적입력 ]")
  
  name = input("등록할 학생의 이름을 입력하세요.>> ")
  kor = int(input("국어 성적을 입력하세요.>> "))
  eng = int(input("영어 성적을 입력하세요.>> "))
  math = int(input("수학 성적을 입력하세요.>> "))
  total = kor + eng + math
  avg = total / 3

  sql = """
    INSERT INTO students
      (no, name, kor, eng, math, total, avg)
    VALUES
      (students_seq.NEXTVAL, :1, :2, :3, :4, :5, :6)
  """
  modify_query_db(sql, [name, kor, eng, math, total, avg])
  print("저장되었습니다.")

def output_students():
  print("[ 학생성적출력 ]")
  
  sql = "SELECT * FROM students ORDER BY no"
  
  rows = select_query_db(sql)
  print_students(rows)

def output_student():
  print("[ 학생성적검색 ]")
  search = input("찾고자 하는 학생 이름을 입력하세요.>> ")

  sql = "SELECT * FROM students WHERE name LIKE :search ORDER BY no"

  rows = select_query_db(sql, [f"%{search}%"])
  print_students(rows)

while True:
  choice = print_menu()

  if choice == "1":
    input_student()
  elif choice == "2":
    output_students()
  elif choice == "3":
    output_student()
  elif choice == "4":
    print("프로그램을 종료합니다.")
    break