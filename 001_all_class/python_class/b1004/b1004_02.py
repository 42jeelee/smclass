import random

RED_COLOR = "\033[0;31m"
GREEN_COLOR = "\033[0;32m"
YELLOW_COLOR = "\033[0;33m"
BLUE_COLOR = "\033[0;34m"
BOLD_COLOR = "\033[1m"
CLEAR_ANSI = "\033[0m"

# 랜덤숫자 : 1-100
r_num = random.randint(1,100)

# 10번도전에서
# 입력한 숫자가 더 크면 작은수를 입력하셔야 합니다.
# 입력한 숫자가 더 작으면 큰수를 입력하셔야 합니다.
# 10번 도전해서 맞추지 못하면, 10번도전에 실패했습니다. 랜덤숫자 : 10
# 도전에 성공했습니다. 랜덤숫자 : 10

cnt = 0
while cnt<10:
  cnt += 1
  num = int(input(BLUE_COLOR+BOLD_COLOR+f"[{cnt}번째 도전] 숫자를 입력하세요.> "+CLEAR_ANSI))
  if num>r_num:
    print(YELLOW_COLOR+"입력한 숫자가 더 큽니다. 작은수를 입력하세요."+CLEAR_ANSI)
  elif num<r_num:
    print(YELLOW_COLOR+"입력한 숫자가 더 작습니다. 큰수를 입력하세요."+CLEAR_ANSI)
  else:
    print(GREEN_COLOR+BOLD_COLOR+"도전에 성공했습니다.", end=' ')
    break
if cnt >= 10:
  print(RED_COLOR+BOLD_COLOR+"10번도전에 실패했습니다.", end=' ')
print("랜덤숫자 :"+CLEAR_ANSI, r_num)