from django.shortcuts import render
from member.models import Member

def m2(request):
  if request.method == "GET":
    memberId = request.COOKIES.get('memberId', '')
    money = request.COOKIES.get('money', '')
    option = request.COOKIES.get('option', '')
    context = {'memberId': memberId, 'money': money, 'option': option}
    return render(request, 'm2.html', context)
  else:
    response = render(request, 'index.html')

    memberId = request.POST.get('memberId')
    money = request.POST.get('money')
    option = request.POST.get('option')
    saveMember = request.POST.get('saveMember')
    
    if saveMember is not None:
      response.set_cookie('memberId', memberId)
      response.set_cookie('money', money)
      response.set_cookie('option', option)
    else:
      response.delete_cookie('memberId', memberId)
      response.delete_cookie('money', money)
      response.delete_cookie('option', option)

    return response

def product(request):
  if request.method == 'GET':
    pId = request.COOKIES.get('pId', '')
    pName = request.COOKIES.get('pName', '')
    context = {"pId": pId, "pName": pName}
    return render(request, 'product.html', context)
  else:
    response = render(request, 'index.html')
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    pOption = request.POST.get('pOption')
    saveProduct = request.POST.get('saveProduct')

    if saveProduct is not None:
      response.set_cookie('pId', pId)
      response.set_cookie('pName', pName)
    else:
      response.delete_cookie('pId')
      response.delete_cookie('pName')

    return response

def login2(request):
  if request.method == 'GET':
    cookId = request.COOKIES.get('cookId')
    context = {'cookId': cookId}
    return render(request, 'login2.html', context)
  else:
    response = render(request, 'index.html')
    # 3개 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    if saveId is not None:
      response.set_cookie('cookId', id)
    else:
      response.delete_cookie('cookId')

    return response



# 로그인페이지
## 쿠키정보검색 : request.COOKIES.get('이름')
## 쿠키저장 : response.set_cookie('key','value')
## 쿠키삭제 : response.delete_cookie('key')
def login(request):
  if request.method == "GET":
    print("쿠키정보 : ",request.COOKIES)
    print("cookinfo 쿠키정보 : ",request.COOKIES.get('cookinfo'))
    saveId = request.COOKIES.get("saveId", "")
    context = {'saveId': saveId}
    response = render(request,'login.html', context)
    # 쿠키 설정(저장)
    # max_age가 없으면 브라우저 종료시 삭제, max_age=60초*60분 삭제  1달 = 60초*60분*24시간*30일
    ## 쿠키정보 검색
    if not request.COOKIES.get('cookinfo'):
      response.set_cookie('cookinfo','1111',max_age=60*60)
    return response
  else:
    print("쿠키정보 : ",request.COOKIES)
    id = request.POST.get("id")
    pw = request.POST.get('pw')
    # pw = request.POST['pw'] # 값없을 경우 에러발생
    saveId = request.POST.get("saveId", "")
    print("전달받은 정보 :",id,pw,saveId)
    response = render(request,'login.html')
    if saveId is not None:
      response.set_cookie('saveId', id, max_age=60*60) # 아이디 기억하기 체크가 있으면 쿠키저장
    else:
      response.delete_cookie('saveId')  # 아이디 기억하기 체크가 없으면 삭제

    return response

# 회원전체리스트 페이지
def mlist(request):
  qs = Member.objects.all()
  context = {"mlist":qs}
  return render(request,'mlist.html',context)