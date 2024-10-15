# 기본매개변수로 값전달 - return 필요, 값전달 필요
def plus(a):
  a = 100
  print("지역변수 a :", a) # 100

a = 10 # 전역변수
plus(a)
print("전역변수 a :",a)

# 복합매개변수로 값 전달 - 리스트,딕셔너리, return필요없음.
# def plus(a):
#   a[0] = 100
#   a[1] = 200
#   print("지역변수 a :",a)

# a = [10,20]
# plus(a)
# print("전역변수 a :",a)
