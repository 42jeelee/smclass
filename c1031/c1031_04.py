### 입력한 달 이상의 입사한 사원을 출력하시오.
import oracledb

def connects():
  try: conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
  except Exception as e: print("예외처리 :", e)
  return conn

d_day = int(input("숫자를 입력하세요.>> "))

conn = connects()
cursor = conn.cursor()

sql = "SELECT * FROM employees WHERE SUBSTR(hire_date, 4, 2) >= :month"
cursor.execute(sql, month=d_day)

rows = cursor.fetchall()

print(f"총 {len(rows)}명")
print("-"*80)
for row in rows:
  print(row[0], row[1])

conn.close()
