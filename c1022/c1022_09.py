n_lists = [
  ["john",100,4.5,1000],
  ["park",80,4.2,800],
  ["lee",90,4.4,2000],
  ["trumf",200,4.7,10],
  ["bill",300,4.3,30]
]

print("기본 :",n_lists)
n_lists.sort(key=lambda x:x[0],reverse=True)
print("금액정렬 :",n_lists)

# a = ""
# print(int(a))
# print("완료")

# a = "안녕하세요"
# print(a[1:])