# 25개 1차원 리스트 -> 1,25 입력한 후 랜덤으로 다시 출력하시오.
# [5,5] 2차원 리스트

import random

aArr = []
for i in range(25):
  aArr.append(i+1)

# print(aArr)

random.shuffle(aArr)

a_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(aArr[5*i+j])
  a_list.append(a)

# print(a_list)
# 리스트를 출력하시오.
while True:
  print("  |\t0\t1\t2\t3\t4")
  print("-"*60)
  for i in range(5):
    print(i,"|",end='\t')
    for j in range(5):
      print(a_list[i][j],end='\t')
    print()
  
  # 값을 입력하면, 해당좌표를 출력하시오.
  re = int(input("값을 입력하세요.(1-25)>> "))
  if not 1 <= re <= 25:
    print("1에서 25사이의 값을 입력하셔야 합니다.")
    continue
  for i in range(5):
    for j in range(5):
      if re == a_list[i][j]:
        print(f"좌표값 :({i,j})")
        a_list[i][j] = 0
        break

  # re = input("좌표를 입력하세요.(0.0) >> ")
  # result = re.split(".")
  # print("좌표 값 :",a_list[int(result[0])][int(result[1])])