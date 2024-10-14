subName = ["국어","영어","수학"]
score = {"국어":100,"영어":95,"수학":80}
print(score)
print(score['국어'])
print(subName[0])
print(score[subName[0]])

for k,v in score.items():
  print(k,":",v)

# for i in subName:
#   print(i,":",score[i])

# def gugudan(end):
#   for i in range(2,end+1):
#     print(f"[ {i}단 ]")
#     for j in range(1,10):
#       print(f"{i} x {j} = {i*j}")
#     print()

# nArr = [9,5,7]

# 2-9,2-5,2-7
# gugudan(9)
# gugudan(5)
# gugudan(7)

# for i in nArr:
#   gugudan(i)
#   print("-"*50)

# # 구구단을 출력하시오.
# def gugudan(st,end):
#   for i in range(st,end+1):
#     print(f"[ {i}단 ]")
#     for j in range(1,10):
#       print(f"{i} x {j} = {i*j}")
#     print()
# # 2-5
# gugudan(2,5)
# # 3-9
# gugudan(3,9)
# # 5-8
# gugudan(5,8)