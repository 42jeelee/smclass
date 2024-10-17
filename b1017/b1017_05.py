  

# 딕셔너리로 학생을 입력하시오.
students = []
sub = ['id','name','kor','eng','math','total','avg','rank']

def print_obj(obj, obj_header):

  print(end='\t')
  for i in obj_header:
    print(i,end='\t')
  print()
  print("-"*80)

  if len(obj)>0:
    for i,o in enumerate(obj):
      print(i,end='\t')
      for j in o.values():
        print(j,end='\t')
      print()
  else:
    print("[ 빈 리스트 ]")
  

f = open('b1017/students.csv','r',encoding='UTF-8')
while True:
  line = f.readline()
  if not line: break
  s = line.strip().split(',')
  # ['20','rdumphreysj','50','75','48','173','57.6666666667','1']
  for idx,i in enumerate(s):
    if idx == 1 : continue
    elif idx == 6: s[idx] = float(i)
    else: s[idx] = int(i)
  students.append(dict(zip(sub,s)))
f.close()

print_obj(students,sub)
