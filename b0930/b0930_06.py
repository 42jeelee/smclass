stu_data = ['홍길동',100,100,100,99]

# for s in stu_data:
#   print(s)

stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [
  [1,'유관순',100,100,100,99],
  [2,'이순신',100,99,98,99],
  [3,'김구',80,100,90,99]
]

# 학생데이터에서 합계, 평균을 추가해서 1줄로 출력하시오.
print("                     [ 학생성적 프로그램 ]")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
#     stu_title[0],stu_title[1],stu_title[2],stu_title[3],
#     stu_title[4],stu_title[5],stu_title[6],stu_title[7]))
# print("-"*60)
for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print()
print("-"*60)
for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(
    s[0],s[1],s[2],s[3],s[4],s[5],
    s[2]+s[3]+s[4]+s[5],
    (s[2]+s[3]+s[4]+s[5])/4
  ))
  # print('\t'.join(map(str,s)), s[2]+s[3]+s[4]+s[5], (s[2]+s[3]+s[4]+s[5])/4, sep="\t")
  # print("{},{},{},{},{},{},{}".format(s[0],s[1],s[2],s[3],s[4],s[1]+s[2]+s[3]+s[4],(s[1]+s[2]+s[3]+s[4])/4))

# 이순신의 평균을 출력하시오.
# print("이순신의 평균 : {}".format((stu_datas[1][1]+stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4])/4))

# 학생이름 : 홍길동
# 국어 : 100
# 영어 : 100
# 수학 : 100
# 과학 : 99
# 합계 :
# 평균 :
 
# print(f"학생이름 : {stu_data[0]}\n국어 : {stu_data[1]}\n영어 : {stu_data[2]}\n수학 : {stu_data[3]}\n과학 : {stu_data[4]}\n합계 : {stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4]}\n평균 : {(stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4])/4}\n")

# print("""
# 학생이름 : {}
# 국어 : {}
# 영어 : {}
# 수학 : {}
# 과학 : {}
# 합계 : {}
# 평균 : {}
# """.format(stu_data[0],stu_data[1],stu_data[2],stu_data[3],stu_data[4],stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4],(stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4])/4))

# 1번에 2개의 길이를 입력받아, 삼각형의 넓이, 직사각형의 넓이를 구하시오.
# length = input("2개의 길이를 입력하세요.")
# print(length.split(" "))

# l_list = length.split(" ")

# print("삼각형의 넓이 : {}".format(float(l_list[0])*float(l_list[1])*0.5))
# print("사각형의 넓이 : {}".format(float(l_list[0])*float(l_list[1])))


# 원의 넓이 : 반지름 * 반지름 * 3.14
# 반지름을 입력받아, 원의 넓이를 구하시오.
# r = float(input("반지름을 입력하세요."))
# area = r ** 2 * 3.14
# print("원의 넓이 :",area)
# print("원의 넓이 : {:.1f}".format(area))

### 복합대입연산자 +=, -=, /=, //=, %=, **=
# a = 10
# a += 5;print(a)
# a -= 5;print(a)
# a *= 5;print(a)
# a /= 5;print(a)
# a //= 5;print(a)
# a %= 5;print(a)
# a **= 5;print(a)

#### 숫자를 문자열로 변환 ####
# 문자열 + 숫자 : 불가능
# a = 100
# b = 10
# print(str(a)+str(b))

#### 문자형숫자 변환 ####
# a = "100"
# b = "10.5"
# c = "안녕"
# print(float(a)) # 정수형 문자열 -> 정수타입 변경가능
# print(int(b)) # 실수형 문자열 -> 실수타입 변경가능
# print(float(c)) # 글자는 숫자형타입으로 변경불가


# aa = 10
# bb = 5

# 여러줄을 1줄 형태로 표현
# # 1줄 선언 방식
# a=10;b=5

# # 1줄 선언 방식
# c,d = 10,20
# s1,s2,s3=1,2,3

# x = 1,2,3,4,5,6,7,...10
# 1
# x = 11,12,13,...20
# 2
# x = 21,22,23,...30
# 3


# 특정숫자 a= 0,1,2,3,4,5
# 1,3,5,7,9
# 2x+1

#### 우선순위 ####
# print(2 + 2 - 2 * 2 / 2 * 2)
# print((2 + 2) - (((2 * 2) / 2) * 2))

# a = 5; b = 3 # 1줄형태로 표현시 ; 넣어주면 됨.
# # /, %, //, **
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)
# print("{},{},{},{}".format(a/b,a%b,a//b,a**b))