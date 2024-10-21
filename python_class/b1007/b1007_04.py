import random

# 1,25 사이의 랜덤숫자를 생성해서 출력하시오.
# num = int(random.random()*25)+1
num2 = random.randint(1,25)
a_list = []
# 25번 반복해서 1,25까지 랜덤숫자를 입력, 중복은 제거하고 출력을 하시오.
# for i in range(25):
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)

# 1-25까지 랜더으로 배치
# while len(a_list)<25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)
# print(a_list)
# print(len(a_list))

# 1-25까지 랜덤으로 배치 - random.sample()
# 범위 리스트, 25개 추출(중복추출 가능)
# a_list = []
# for i in range(25):
#   a_list.append(i+1)

# b_list = random.choices(a_list,k=25)

