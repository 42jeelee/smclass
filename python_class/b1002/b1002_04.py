# from datetime import datetime
# today = datetime.now()

import datetime
today = datetime.datetime.now()

# if 12시 이상이면 오후, 오전이라고 출력하시오.
if today.hour >= 12:
  print("오후입니다.")
else:
  print("오전입니다.")

# print("{}년 {}월 {}일 {}시 {}분 {}초".format(today.year,
#      today.month,today.day,today.hour,today.minute,today.second))
# print(today.year, "년")
# print(today.month, "월")
# print(today.day, "일")
# print(today.hour, "시")
# print(today.minute, "분")
# print(today.second, "초")
