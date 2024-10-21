import os

# f = open('b1017/cart.txt','r',encoding='utf-8')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line.strip())

# isfile : 파일인지확인, isdir : 디렉토리인지 확인, exists : 파일이 존재하는지
# if os.path.exists('b1017/students.txt'):
#   print("파일이 존재합니다.")
# else:
#   print("파일이 존재하지 않습니다.")

# product = [
#   {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
#   {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
#   {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
#   {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
# ]

# f = open('b1017/products.csv','w',encoding='UTF-8')

# for p in product:
#   f.write(','.join([ str(i) for i in p.values() ])+'\n')

# f.close()