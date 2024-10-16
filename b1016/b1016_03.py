# students = [
#   [1,"홍길동",100,100,100,300,100.00,0],
#   [2,"유관순",100,100,100,300,100.00,0],
#   [3,"이순신",100,99,90,96.3333333333333,0],
# ]
stu_key = ['no','name','kor','eng','math','total','avg','rank']
students = []

# 파일읽기 - r
f = open('b1016/a.txt','r',encoding='UTF-8')
while True:
  line = f.readline()
  if not line: break
  s = line.strip().split(',')
  # s[0] = int(s[0])
  # s[2] = int(s[2])
  # s[3] = int(s[3])
  # s[4] = int(s[4])
  # s[5] = int(s[5])
  # s[6] = float(s[6])
  # s[7] = int(s[7])
  for i in range(len(s)):
    if i == 1: continue
    elif i == 6: s[i] = float(s[i])
    else: s[i] = int(s[i])
  students.append(dict(zip(stu_key,s)))
  print(line.strip())

print(students)
f.close()