from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def join1(request):
  return render(request, "join01_terms.html")

def join2(request):
  return render(request, "join02_info_input.html")

def join3(request):
  return render(request, "join03_success.html")

def logout(request):
  request.session.clear()

  return redirect("member:login")

def login(request):
  c_saveId = request.COOKIES.get('c_saveId', '')
  msg = ""

  if request.method == "GET":
    return render(request, "login.html", {"c_saveId": c_saveId, "msg": msg})
  
  id = request.POST.get("id")
  pw = request.POST.get("pw")
  saveId = request.POST.get("saveId")

  member = Member.objects.filter(id=id, pw=pw)

  if len(member) == 0:
    msg = "아이디 또는 비밀번호가 일치하지 않습니다."
    return render(request, "login.html", {"c_saveId": c_saveId, "msg": msg})

  response = redirect("/")

  request.session['session_id'] = id
  request.session['session_nickname'] = member[0].nickname
  
  if saveId is not None:
    response.set_cookie('c_saveId', id)
  else:
    response.delete_cookie('c_saveId')

  return response
