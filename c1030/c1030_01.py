import oracledb
import random
import smtplib
from email.mime.text import MIMEText

def connects():
  conn = None
  try:
    conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
  except Exception as e:
    print("예외발생:", e)
  return conn

def create_pw():
  n = random.randrange(0, 10000)
  return f"{n:04}"

while True:
  print("[ 커뮤니티]")
  print("1. 로그인")
  print("2. 비밀번호 분실")
  print("3. 회원가입")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.>> ")

  if choice == "1":
    user_id = input("아이디를 입력하세요.>> ")
    user_pw = input("패스워드를 입력하세요.>> ")
    # db 접속
    conn = connects()
    cursor = conn.cursor()
    sql = "SELECT * FROM member WHERE id=:id AND pw=:pw"
    cursor.execute(sql, id=user_id, pw=user_pw)
    row = cursor.fetchone()
    if row is not None:
      print(f"로그인 성공! {row[2]}님 환영합니다.")
    else:
      print("아이디 또는 패스워드가 일치하지 않습니다. 정확히 입력하세요!! ")
      continue
    conn.close()

    # 오라클db에 접속해서 member 테이블에서 가져옴.

    # if user_id == "aaa" and user_pw == "1111":
    #   print("로그인 성공")
    # else:
    #   print("로그인 실패")
    #   continue
    
    print("[ 학생성적 프로그램에 접속합니다. ]")
    ### 프로그램 구현 ###

  elif choice == "2":
    print("[ 비밀번호 찾기 ]")
    search = input("해당 아이디를 입력하세요.>> ")
    # 아이디 있는지 확인
    conn = connects()
    cursor = conn.cursor()
    sql = "SELECT * FROM member WHERE id=:id"
    cursor.execute(sql, id=search)
    row = cursor.fetchone()
    if row is not None:
      print("아이디가 존재합니다. 임시 패스워드를 발급합니다.")
      # 1. 임시 비밀번호 생성해서
      # 2. 이메일로 보냅니다.
      # 3. 아이디에 비밀번호를 임시비밀번호를 수정합니다.
      # 4. 임시 번호로 로그인을 했을 경우 로그인 성공이 나타나도록 하시오.

      new_pw = create_pw()

      cursor.execute("UPDATE member SET pw=:pw WHERE id=:id", id=row[0], pw=new_pw)
      conn.commit()

      msg = MIMEText(f"임시 비밀번호 : {new_pw}")
      msg['Subject'] = "임시 비밀번호를 발급 안내"
      msg['From'] = "kaimahi@naver.com"
      msg['To'] = "jeelee553@gmail.com" # row[3]

      s = smtplib.SMTP("smtp.naver.com",587)
      s.starttls()
      s.login(msg['From'],"ZV18TYVWT39V")
      s.sendmail(msg['From'],msg['To'],msg.as_string())
      s.quit()

    else:
      print("아이디가 존재하지 않습니다.")

    conn.close()
  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break