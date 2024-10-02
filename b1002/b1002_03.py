# if - else
# if elif else
# 100~98 A+
# 97~94 A
# 93~90 A-

# 89~88 B+
# 87~84 B
# 83~80 B-

# 70점대 C
# 79~78 C+
# 77~74 C
# 73~70 C-

# 60점대 D
# 60점미만 F
num = int(input("점수를 입력하세요."))
score = ""
if num == 100:
  score += "A+"
elif 90 <= num < 100:
  score += "A"
elif 80 <= num:
  score += "B"
elif 70 <= num:
  score += "C"
elif 60 <= num:
  score += "D"
else:
  score += "F"

if 60 < num < 100:
  if 8 <= num%10 <= 9:
    score += "+"
  elif 0 <= num%10 <= 3:
    score += "-"

print(score)

# 숫자를 입력받아
# 3,4,5 - 봄, 6,7,8 - 여름, 9,10,11 - 가을, 12,1,2 - 겨울입니다.
# 그 외 숫자 - 잘못된 월이 입력되었습니다. 출력하시오.
# month = int(input("월을 입력하세요."))
# if 3 <= month <= 5:
#   print("봄입니다.")
# elif 6 <= month <= 8:
#   print("여름입니다.")
# elif 9 <= month <= 11:
#   print("가을입니다.")
# elif 12 == month or 1 <= month <= 2:
#   print("겨울입니다.")
# else:
#   print("잘못된 월이 입력되었습니다.")



# 입력한 숫자가 10(포함)보다 작거나, 100(포함)보다 클 때 정답입니다. 오답입니다.
# 출력하시오.
# num = int(input("숫자를 입력하세요."))
# if 10 <= num or num >= 100:
#   print("정답입니다.")
# else:
#   print("오답입니다.")

# 입력한 숫자가 1(포함)보다 크고 10(포함)보다 작을때만 정답입니다. 오답입니다.
# 1 <= x <= 10
# 정답입니다. 오답입니다.
# num = int(input("숫자를 입력하세요."))
# if 1 <= num and num <= 10:
#   print("정답입니다.")
# else:
#   print("오답입니다.")

# if 1<=num<=10:
#   print("정답입니다.")
# else:
#   print("오답입니다.")

# 입력한 숫자가 짝수인지, 홀수인지 출력하시오.
# num = int(input("숫자를 입력하세요."))

# if num%2 == 0:
#   print("짝수입니다.")
# else:
#   print("홀수입니다.")