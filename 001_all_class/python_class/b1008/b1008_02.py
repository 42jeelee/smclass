# [0,3,6,9,12,...,57]
aArr = []
for i in range(20):
  aArr.append(i*3)
# print(aArr)

# 2차원 리스트 [4,5]
a_list = []
for i in range(4):
  a = []
  for j in range(5):
    a.append(aArr[5*i+j])
  a_list.append(a)

print(a_list)

# [4,5] 2차원 리스트
# a_list = []

# for i in range(4):
#   a = []
#   for j in range(5):
#     a.append(15*i+j*3)
#   a_list.append(a)
# # print(a_list)

# for i in a_list:
#   for j in i:
#     print(j,end='\t')
#   print()