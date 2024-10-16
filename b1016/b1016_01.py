# 파일 with
with open('b1016/aa.txt','w',encoding='UTF-8') as f:
  f.write("안녕하세요.")

# 파일 이어쓰기 - a
# while True:
#   print("[ 메모장 ]")
#   data = input("저장하려는 글자를 입력하세요.>> ")
#   f = open('b1016/aa.txt','a',encoding='UTF-8')
#   f.write(data+'\n')
#   f.close()

# 파일쓰기 - w : 파일생성후 글자 입력

# while True:
#   print("[ 메모장 ]")
#   data = input("저장하려는 글자를 입력하세요.>> ")
#   f = open('b1016/aa.txt','w',encoding='UTF-8')
#   f.write(data)
#   f.close()

# f = open('b1016/aa.txt','w',encoding='UTF-8')
# for i in range(1,11):
#   data = f"안녕하세요. {i}\n"
#   f.write(data)
# f.close()
# print("글쓰기 종료")

# f = open('b1016/aa.txt','w',encoding='UTF-8')
# f.write("안녕하세요.1\n")
# f.write("안녕하세요.2\n")
# f.write("안녕하세요.3\n")
# f.close()
# print("글쓰기 종료")

# 파일읽기 - r
# 위치에 파일이 없으면 에러

# 3. read()
# f = open('b1016/a.txt','r',encoding="UTF-8")
# # print(type(f))
# for line in f:
#   print(line.strip())
# f.close()

# # 2. readlines() - 모든글을 읽어오기
# f = open('b1016/a.txt','r',encoding='UTF-8')
# lines = f.readlines()
# for line in lines:
#   print(line.strip())

# f.close()

# 1. readline() - 1줄씩 읽어오기
# f = open("b1016/a.txt",'r',encoding='UTF-8')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line.strip()) # \n 값을 생략
# f.close()