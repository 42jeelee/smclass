# 웹스크래핑 세팅
import requests

res = requests.get("https://www.google.com/") # html소스를 가져옴
res = requests.get("https://www.naver.com/") # html소스를 가져옴
# res = requests.get("https://www.melon.com/index.htm") # html소스를 가져옴
res.raise_for_status() # 에러시 종료

# requests 정보를 가져올시
# 제이쿼리,자바스크립트,외부페이지,react,vue.. 비동기식으로 작동되는 소스는
# 가져오지 못함.

print("총 문자 길이 :",len(res.text))

# 파일 저장
# f = open("c1021/a.html","w",encoding="UTF-8")
# f.write(res.text)
# f.close()

# f.close()
# with open("c1021/a.html","w",encoding="UTF-8") as f:
#   f.write(res.text)

# print("응답코드 :",res.status_code) # 200
# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할 수 없습니다.")