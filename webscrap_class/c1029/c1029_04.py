import datetime
import oracledb

# db연결 함수선언
def connection():
  try:
    conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
    print("db연결 :", conn.version)
  except Exception as e: print("예외 발생 :", e)
  return conn

# 함수 호출
conn = connection()
cursor = conn.cursor()

# 범위를 입력받아서 그 사이의 사원을 출력하시오.
num1 = input("최소 연봉을 입력하세요 >> ")
num2 = input("최대 연봉을 입력하세요 >> ")

# 월급이 4000 ~ 8000 사이의 사원을 모두 출력하시오.
sql = "SELECT employee_id, emp_name, salary FROM employees WHERE :1 <= salary AND salary <= :2 ORDER BY salary"
cursor.execute(sql, [num1, num2])

title = ['employee_id', 'emp_name', 'salary']
a_list = [] # dict타입으로 변경해서 저장하시오.
rows = cursor.fetchall()

a_list = list(map(lambda x: dict(zip(title, x)), rows))
print(a_list)

# 입력한 값을 가지고 이름이 포함되어 있는 데이터를 출력하시오.
# search = input("이름을 입력하세요.>> ")
# search = '%' + search + '%'
# sql = "SELECT * FROM employees WHERE emp_name LIKE :search"
# cursor.execute(sql,search=search)
# 검색한
# search = input("번호검색 >> ")

# employees 테이블에서 이름이 a가 포함되어 있는 이름, 모든 컬럼 출력
# sql = "SELECT * FROM employees WHERE employee_id >= :1"
# cursor.execute(sql, [search])
# sql = "SELECT * FROM employees WHERE employee_id >= :search"
# cursor.execute(sql, search=search)


# search = input("검색할 이름을 입력하세요.> ")

# # employees 테이블에서 이름이 a가 포함되어 있는 이름, 모든 컬럼 출력
# sql = "SELECT * FROM employees WHERE emp_name LIKE :1"
# cursor.execute(sql, [f"%{search}%"])

# titles = ['번호', '이름', '이메일', '폰번호', '고용일', '연봉', '매니저', '커미션', '퇴직일', '부서', '직업', '등록일', '수정일']
# for title in (titles[:2] + [titles[5]]):
#   print(title, end='\t')
# print()
# print("-"*100)

# rows = cursor.fetchall()
# for row in rows:
#   for r in row:
#     if isinstance(r, datetime.datetime):
#       r = r.strftime("%y/%m")
#     print(r, end='\t')
#   print()

conn.close()