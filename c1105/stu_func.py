import oracledb

RED_COLOR = "\033[0;31m"
GREEN_COLOR = "\033[0;32m"
YELLOW_COLOR = "\033[0;33m"
BLUE_COLOR = "\033[0;34m"
BOLD_COLOR = "\033[1m"
CLEAR_ANSI = "\033[0m"
CLEAR_CONSOLE = "\033[2J\033[H"

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

def modify_query_db(sql, values = None):
  conn = connects()
  cursor = conn.cursor()
  if values is not None: cursor.execute(sql, values)
  else: cursor.execute(sql)
  conn.commit()
  conn.close()
  
def input_choice(comment, max_num):
  while True:
    try:
      num = int(input(YELLOW_COLOR + BOLD_COLOR + comment + CLEAR_ANSI))

      if num <= max_num:
        return num
      print(RED_COLOR + f"{max_num}보다 작은 수만 입력 가능합니다. 다시 입력하세요." + CLEAR_ANSI)
    except:
      print(RED_COLOR + "숫자만 입력이 가능합니다." + CLEAR_ANSI)

def print_menu():
  print(CLEAR_CONSOLE + BLUE_COLOR + BOLD_COLOR, end='')
  print("[ 학생성적프로그램 ]" + CLEAR_ANSI)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적검색")
  print("4. 학생성적정렬") # 이름순차정렬, 이름역순정렬, 합계순차정렬, 합계역순정렬
  print("5. 등수처리")
  print("6. 학생성적수정")
  print("7. 종료")
  print("-"*50)
  return input_choice("원하는 번호를 입력하세요.>> ", 7)

def print_students(students):
  COLUMN_TITLE = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']

  print(CLEAR_CONSOLE + GREEN_COLOR + BOLD_COLOR, end='')
  for i, t in enumerate(COLUMN_TITLE):
    if i == 1: t = f"{t:20s}"

    print(t, end='\t')
  print(CLEAR_ANSI)
  print("-"*100)

  for student in students:
    for i, s in enumerate(student):
      if i == 1: s = f"{s:20s}"

      print(s, end='\t')
    print()

def input_student():
  print(CLEAR_CONSOLE + BLUE_COLOR + BOLD_COLOR, end='')
  print("[ 학생성적입력 ]" + CLEAR_ANSI)
  
  name = input("등록할 학생의 이름을 입력하세요.>> ")
  kor = int(input("국어 성적을 입력하세요.>> "))
  eng = int(input("영어 성적을 입력하세요.>> "))
  math = int(input("수학 성적을 입력하세요.>> "))
  total = kor + eng + math
  avg = total / 3

  sql = """
    INSERT INTO students VALUES
      (students_seq.NEXTVAL, :1, :2, :3, :4, :5, :6, 0, SYSDATE)
  """
  modify_query_db(sql, [name, kor, eng, math, total, avg])
  print("저장되었습니다.")

def output_students():
  print(CLEAR_CONSOLE + BLUE_COLOR + BOLD_COLOR, end='')
  print("[ 학생성적출력 ]" + CLEAR_ANSI)
  
  sql = """
    SELECT
      no, name, kor, eng, math, total, ROUND(avg, 2), rank, TO_CHAR(sdate, 'yyyy-mm')
    FROM
      students
    ORDER BY
      no
  """
  
  rows = select_query_db(sql)
  print_students(rows)

def output_student():
  print(CLEAR_CONSOLE + BLUE_COLOR + BOLD_COLOR, end='')
  print("[ 학생성적검색 ]" + CLEAR_ANSI)
  search = input("찾고자 하는 학생 이름을 입력하세요.>> ")

  sql = "SELECT * FROM students WHERE name LIKE :search ORDER BY no"

  rows = select_query_db(sql, [f"%{search}%"])
  print_students(rows)

def sort_students():
  print(CLEAR_CONSOLE + BLUE_COLOR + BOLD_COLOR, end='')
  print("[ 학생성적정렬 ]" + CLEAR_ANSI)
  print("1. 이름순차정렬")
  print("2. 이름역순정렬")
  print("3. 합계순차정렬")
  print("4. 합계역순정렬")
  print("5. 취소")
  choice = input_choice("원하는 번호를 입력하세요.>> ", 5)

  arg = ""
  if choice == 1:
    arg = "name"
  elif choice == 2:
    arg = "name DESC"
  elif choice == 3:
    arg = "total"
  elif choice == 4:
    arg = "total DESC"

  sql = f"""
    SELECT
      no, name, kor, eng, math, total, ROUND(avg, 2), rank, TO_CHAR(sdate, 'yyyy-mm')
    FROM
      students
    ORDER BY
      {arg}
  """

  rows = select_query_db(sql)

  print_students(rows)

def rank_students():
  print(CLEAR_CONSOLE + BLUE_COLOR + BOLD_COLOR, end='')
  print("[ 등수처리 ]" + CLEAR_ANSI)
  
  sql = """
    UPDATE students a SET rank = (
      SELECT ranks FROM (
        SELECT no, RANK() OVER(ORDER BY avg DESC) ranks FROM students
      ) b
      WHERE a.no = b.no
    )
  """

  modify_query_db(sql)
  print("등수처리가 완료되었습니다!")


def update_student():
  SUBJECTS_TITLE = ['국어', '영어', '수학']
  SUBJECTS_COLUMN = ['kor', 'eng', 'math']
  SUBJECTS_NUM = len(SUBJECTS_TITLE)

  print(CLEAR_CONSOLE + BLUE_COLOR + BOLD_COLOR, end='')
  print("[ 학생성적수정 ]" + CLEAR_ANSI)
  name = input("수정하고자 하는 학생 이름을 입력하세요.>> ")

  sql = "SELECT * FROM students WHERE name = :name"

  rows = select_query_db(sql, [name])
  if len(rows) > 0:
    row = list(rows[0])
    print(f"{row[1]} 학생을 찾았습니다!")

    print(CLEAR_CONSOLE + BLUE_COLOR + BOLD_COLOR, end='')
    print("[ 수정과목선택 ]" + CLEAR_ANSI)
    for i, s in enumerate(SUBJECTS_TITLE):
      print(f"{i+1}. {s}")
    print(f"{SUBJECTS_NUM}. 취소")
    print("-"*30)
    choice = input_choice("수정과목을 선택하세요.>> ", SUBJECTS_NUM)

    if 1 <= choice <= SUBJECTS_NUM:
      print(f"이전 {SUBJECTS_TITLE[choice - 1]} 성적 : {row[choice + 1]}")

      row[choice + 1] = input_choice("변경할 성적을 입력하세요.>> ", 100)

      row[5] = row[2] + row[3] + row[4]
      row[6] = row[5] / 3

      sql = f"""
        UPDATE students SET
          {SUBJECTS_COLUMN[choice - 1]} = :1, total = :2, avg = :3
        WHERE no = {row[0]}
      """

      modify_query_db(sql, [row[choice + 1], row[5], row[6]])
      print("수정하였습니다!")
      print_students([row])
  else:
    print(RED_COLOR + "해당 학생이 존재하지 않습니다." + CLEAR_ANSI)

