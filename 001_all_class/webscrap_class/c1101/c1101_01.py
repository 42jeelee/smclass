import oracledb
import datetime

nowYear = datetime.datetime.now().year

# db연결 함수선언
def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e:
    print("예외처리 :", e)
  return conn

## 회원 수 확인
def member_count():
  ## oracle db - mem 테이블의 count를 가져오시오.
  conn = connects()
  cursor = conn.cursor()
  
  # employees 테이블 부서번호 50번인 사원 수를 가져오시오.
  # sql = """
  # SELECT COUNT(e.department_id), e.department_id, d.department_name
  # FROM employees e, departments d
  # WHERE e.department_id = d.department_id AND d.department_id = 50
  # GROUP BY e.department_id, d.department_name
  # """
  sql = "SELECT COUNT(*) FROM mem"
  cursor.execute(sql)
  row = cursor.fetchone()
  conn.close()
  return row


## 회원 수 확인 값을 리턴하시오.
all_member = member_count()

print("[ 커뮤니티 ]")
print(f"현재 회원 수 : {all_member[0]}")
print()
print("1. 로그인")
print("2. 회원가입")
print("3. 회원정보수정")
choice = input("원하는 번호를 입력하세요.>> ")

if choice == '1':
  pass
elif choice == '2':
  id = input("아이디를 입력하세요.>> ")
  pw = input("패스워드를 입력하세요.>> ")
  name = input("이름을 입력하세요.>> ")
  birth = input("생년월일을 입력하세요.(예> 20020312)>> ")
  age = nowYear - int(birth[:4]) # 나이 자동계산
  gender = input("성별을 입력하세요.(Male, Female)>> ")
  hobby = input("취미를 입력하세요.>> ")

  my_list = [id, pw, name, age, birth, gender, hobby]
  print(my_list)

  # db접속
  conn = connects()
  cursor = conn.cursor()
  # sql = "INSERT INTO mem (id, pw, name, age, birth, gender, hobby) VALUES (:1, :2, :3, :4, :5, :6, :7)"
  # cursor.execute(sql, my_list)
  sql = "INSERT INTO mem (id, pw, name, age, birth, gender, hobby) VALUES (:id, :pw, :name, :age, :birth, :gender, :hobby)"
  cursor.execute(sql, id=id, pw=pw, name=name, age=age, birth=birth, gender=gender, hobby=hobby)
  conn.commit()
  conn.close()
  print("저장되었습니다.")
elif choice == "3":

  # db접속
  conn = connects()
  cursor = conn.cursor()
  id = "aaa"
  sql = "SELECT * FROM mem WHERE id = :id"
  cursor.execute(sql, id=id)
  row = cursor.fetchone()
  print(f"현재 취미 {row[6]}")

  hobby = input("수정할 hobby를 입력하세요.>> ")
  sql = "UPDATE mem SET hobby = :hobby WHERE id = :id"
  cursor.execute(sql, hobby=hobby, id=id)
  conn.commit()
  conn.close()
  print("수정되었습니다.")