import oracledb

## sql developer 실행
conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")

## sql창이 열림
cursor = conn.cursor()

# sql 작성, 실행
nos = list(map(int, input("숫자 3개를 입력하세요>> ").split()))

# no=10,20,30 을 검색해서 출력하시오.

# excute 함수 : 변수 추가
sql = "SELECT * FROM students WHERE no IN (:1, :2, :3)"
cursor.execute(sql, nos)

# 데이터 가져오기 - fetchone() : 1개, fetchmany() : 숫자만큼, fetchall() : 모든 것
rows = cursor.fetchall()
titles = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수', '등록일']
for title in titles:
  print(title, end='\t')
print()
print("-"*80)

for row in rows:
  for i,r in enumerate(row):
    if i == 1:
      print(f"{r:10}", end="\t")
      continue
    if i == 6:
      print(f"{r:.2f}", end="\t")
      continue
    elif i == 8:
      # strftime()함수 : 날짜포맷함수 %Y : 2024, %y : 24
      print(r.strftime("%y-%m-%d"), end="\t")
      continue
    print(r, end='\t')
  print()
conn.close()