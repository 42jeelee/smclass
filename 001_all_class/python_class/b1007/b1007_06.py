import random

# 25개 1차원 리스트

# 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오.
a_list = [0]*20+[1]*5
random.shuffle(a_list)
print(a_list)

# [5,5] 2차원리스트에 a_list의 값을 입력한후 출력하시오.
b_list = []
for i in range(0,len(a_list),5):
  b_list.append(a_list[i:i+5])

print("   |\t0\t1\t2\t3\t4")
print("-"*50)
for i in range(len(b_list)):
  print(f"{i}  |",end="\t")
  for j in range(len(b_list[i])):
    print(f"{b_list[i][j]}",end="\t")
  print()

x,y = map(int, input("좌표를 입력해주세요.[0,1]> ").split(','))
print(f"({x},{y}) 좌표값 : {b_list[x][y]}")

# 0:20개, 1:5개 생성
# a_list = []
# for i in range(25):
#   if i<20:
#     a_list.append(0)
#   else:
#     a_list.append(1)
