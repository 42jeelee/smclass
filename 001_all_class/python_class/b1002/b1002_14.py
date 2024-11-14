import random

# 1-100까지의 랜덤숫자를 생성
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
# 10번 도전하도록 하시오.
# 정답입니다. 프로그램종료 하시오. break
r_num = random.randint(1,100)
cnt = 0

# while ################################################
# while cnt<10:
#   cnt += 1
#   num = int(input("숫자를 입력하세요."))
#   if num < r_num:
#     print(f"{num}가 작습니다.")
#   elif num == r_num:
#     print(f"{cnt}번째에 정답입니다. 정답번호 : {r_num}")
#     break
#   else:
#     print(f"{num}가 큽니다.")

########################################################

# for ##################################################
for i in range(10):
  num = int(input("숫자를 입력하세요."))
  if num < r_num:
    print(f"{num}가 작습니다.")
  elif num == r_num:
    print(f"{cnt}번째에 정답입니다. 정답번호 : {r_num}")
    break
  else:
    print(f"{num}가 큽니다.")
  cnt += 1

########################################################

if cnt == 10:
  print(f"실패입니다. 정답은 {r_num}.")
