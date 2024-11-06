import random
import oracledb

def connects():
  conn = None
  try:
    conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
  except Exception as e:
    print("예외발생:", e)
  return conn

user_id = input("아이디를 입력하세요.>> ")
user_pw = input("패스워드를 입력하세요.>> ")

conn = connects()
cursor = conn.cursor()
sql = "UPDATE member SET pw=:pw WHERE id=:id"
cursor.execute(sql, id=user_id, pw=user_pw)
conn.commit()

print("파일이 수정되었습니다.")
conn.close()

# 임시 비밀번호 생성
# a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = random.randrange(0, 100000000) # 0-99999999

# ran_num = f"{a:08}"
# 랜덤 4자리 숫자

# print("{:4}".format(a))