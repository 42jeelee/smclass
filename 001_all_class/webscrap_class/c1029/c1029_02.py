import oracledb

## 학생 성적 출력을 하시오.
conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")

cursor = conn.cursor()

sql = "SELECT * FROM students"
cursor.execute(sql)

rows = cursor.fetchall()

titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']

for i,title in enumerate(titles):
  if i == 1:
    title = f"{title:10}"
  print(title, end="\t")
print()
print("-"*80)

for row in rows:
  for i,r in enumerate(row):
    if i == 1:
      r = f"{r:10}"
    elif i == 6:
      r = f"{r:.2f}"
    elif i == 8:
      r = r.strftime("%y-%m-%d")
    print(r, end="\t")
  print()

conn.close()