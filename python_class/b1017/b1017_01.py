subject = ["국어","영어","수학","과학","역사"]
score = []

while True:
  print("1.과목추가")
  print("0.종료")
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == "1":
    s_input = input("과목을 추가하세요.>> ")
    subject.append(s_input)
  elif choice == "0":
    break

for i in range(5):
  score.append(int(input(f"{subject[i]}점수를 입력하세요.>> ")))

sum = 0
for i in range(5):
  print(f"{subject[i]} :",score[i])
  sum += score[i]
print("합계 :",sum)

# num1 = int(input("국어점수를 입력하세요."))
# num2 = int(input("영어점수를 입력하세요."))
# num3 = int(input("수학점수를 입력하세요."))
# num4 = int(input("과학점수를 입력하세요."))
# num5 = int(input("역사점수를 입력하세요."))
# print("국어 :",num1)
# print("영어 :",num2)
# print("수학 :",num3)
# print("과학 :",num4)
# print("역사 :",num5)
# print("합계 :",num1+num2+num3+num4+num5)

# 함수선언
# a = 10
# b = 20
# c = 30

# # a에 함수를 사용해서, a+b+c의 합을 입력해서 출력하시오.
# def add(a,b,c):
#   return a+b+c

# add(a,b,c)
# print(a)

# a = 10
# b = 20
# sum = 0

# def add(a,b):
#   return a+b

# sum = add(a,b) # 함수호출
# print("a+b 합계 :",sum)

# a = 10 # 전역변수

# # 함수선언
# def func():
#   # global a # 전역변수를 가져옴.
#   # a += 50
#   # a = 50 # 지역변수 - 함수를 종료하면 모두 제거됨.
#   print("함수 내 a :",a)

# # 함수호출
# func()
# print("함수 밖 a",a)

# subject = ['국어','영어']

# # 함수선언
# def output(subject):
#   # 출력
#   print("과목")
#   print("-"*20)
#   for s in subject:
#     print(s)

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요.>> ")
#   # list - append
#   subject.append(s_input)
#   output(subject)