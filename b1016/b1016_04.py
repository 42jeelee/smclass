member = [
  {"id":"aaa","pw":"1111","name":"홍길동","nicName":"길동스","address":"서울시","money":100000000},
  {"id":"bbb","pw":"2222","name":"유관순","nicName":"관순스","address":"부산시","money":70000000},
  {"id":"ccc","pw":"3333","name":"이순신","nicName":"순신스","address":"경기도","money":50000000},
  {"id":"ddd","pw":"4444","name":"강감찬","nicName":"감찬스","address":"인천시","money":10000000},
  {"id":"admin","pw":"5555","name":"김구","nicName":"김스","address":"대구시","money":100000000},
]

# memter.txt 파일생성해서 내용을 저장하시오.
f = open('b1016/member.txt', 'w', encoding='utf-8')
for m in member:
  f.write(','.join([str(i) for i in m.values()]) + '\n')
f.close()

# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]
#students 딕셔너리파일을 메모장에 csv파일형태로 저장하시오.

# f = open('b1016/students.txt','w',encoding='utf-8')
# # f.write("1,홍길동,100,100,99,299,99.66666666666667,0\n")
# for s in students:
#   f.write(','.join([str(i) for i in s.values()]) + '\n')
# f.close()
# print("완료되었습니다.")

# students.txt
# 1,홍길동,100,100,99,299,99.66666666666667,0
# 2,유관순,100,100,99,299,99.66666666666667,0
# 3,이순신,100,100,99,299,99.66666666666667,0