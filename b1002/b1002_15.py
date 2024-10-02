import random

BLUE_COLOR = "\033[0;34m"
RED_COLOR = "\033[0;31m"
CLEAR_COLOR = "\033[0m"

r_num = random.randint(1,100)
cnt = 1
while cnt<10:
  cnt += 1
  num = int(input("숫자를 입력하세요."))
  print(f"{BLUE_COLOR}{cnt}번째 도전입니다.{CLEAR_COLOR}", end=' ')
  if num < r_num:
    print(f"{num}가 더 작습니다.")
  elif num > r_num:
    print(f"{num}가 더 큽니다.")
  else:
    print(f"{BLUE_COLOR}정답입니다!{CLEAR_COLOR}", end=' ')
    break

if cnt == 10:
  print(f"{RED_COLOR}실패입니다..{CLEAR_COLOR}", end='')

print(f"정답은 {r_num}입니다.")