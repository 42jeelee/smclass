import random

my_money = 100000

lotto = [0]*6+[1]*3
aa_list = [
  ["로또","로또","로또"],
  ["로또","로또","로또"],
  ["로또","로또","로또"]
]

random.shuffle(lotto)

a_list = []
for i in range(3):
  a = []
  for j in range(3):
    a.append(lotto[3*i+j])
  a_list.append(a)

while my_money>0:
  input_money = int(input(f"얼마를 거시겠습니까?(현재잔액: {my_money})>> "))
  my_money -= input_money

  print("\t0\t1\t2")
  for i in range(3):
    print(i,"|",end='\t')
    for j in range(3):
      print(aa_list[i][j],end='\t')
    print()
  
  x,y = map(int, input("좌표를 입력하세요(0,0)>> ").split(","))
  if a_list[x][y] == 1:
    print("당첨!")
    input_money *= 10
    print(f"당첨금 : {input_money}")
    my_money += input_money
    aa_list[x][y] = "당첨"
  else:
    print("꽝!")
    aa_list[x][y] = "꽝"
    input_money = 0
