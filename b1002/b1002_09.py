fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
fruits = fruit.split(",")
print(fruits)
print(len(fruits))
# 리스트 인 경우 검색해서 해당되는 index를 출력하시오.
# 배 에 해당되는 index번호를 출력
search = input(">")
if search in fruits:
  print("배의 개수 :", fruits.count(search))
  for idx,f in enumerate(fruits):
    if f == search:
      print(idx)


# print(fruit.find("배", 0)) # 3
# print(fruit.find("배", 3+1))
# print(fruit.find("배", fruit.find("배", 0)+1)) # 15
# print(fruit.find("배", 15+1))
# print(fruit.find("배", fruit.find("배", fruit.find("배", 0)+1)+1))

# print(fruit.find("딸기", 0)) # 5
# print(fruit.find("딸기", fruit.find("딸기", 0)+1))
# print(fruit.find("딸기", 6))