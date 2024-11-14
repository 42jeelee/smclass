# for문을 출력
for k in range(2,10):
  print(f"[ {k} 단 ]", end="\t")
print()
for i in range(2,10):
  for j in range(1, 10):
    print(f"{j} x {i} = {i*j}",end="\t")
  print()


# 000
# 001
# ...
# 997
# 998
# 999

# for i in range(10):
#   for j in range(10):
#     for k in range(10):
#       print(f"{i}{j}{k}")

# for i in range(1000):
#   print(f"{i:03d}")

# j,k = 0,0
# for i in range(1000):
#   print(f"{k}{j}{i%10}")
#   if i%10 == 9:
#     j += 1
#   if j == 10:
#     j = 0
#     k += 1
#     if k == 10:
#       break
    

# 구구단 입력한 단까지 출력하시오. 3 -> 1,2,3단 출력 5-> 1,2,3,4,5단까지 출력
# num = int(input("몇단까지 출력하시겠습니까? "))
# for i in range(1,num+1):
#   print(f"[ {i} 단 ]")
#   for j in range(1, 10):
#     print(f"{i} x {j} = {i*j}")
