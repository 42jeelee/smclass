from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def register(request):
  if request.method == "GET":
    return render(request, 'register.html')
  
  id = request.POST.get('id')
  pw = request.POST.get('pw')
  name = request.POST.get('name')
  nickname = request.POST.get('nickname')
  tel = request.POST.get('tel')
  gender = request.POST.get('gender')
  hobby = ','.join(request.POST.getlist('hobby'))

  member = Member.objects.create(id=id, pw=pw, name=name, nickname=nickname, tel=tel, gender=gender, hobby=hobby)
  member.save()

  return redirect('index')

def logout(request):
  request.session.clear()
  return redirect('member:login')

def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  
  id = request.POST.get('id')
  pw = request.POST.get('pw')

  members = Member.objects.filter(id=id, pw=pw)
  if len(members) > 0:
    member = members[0]

    request.session['session_id'] = id
    request.session['session_nickname'] = member.nickname
  else:
    context = {"emsg": "아이디 또는 비밀번호가 일치하지 않습니다."}
    return render(request, 'login.html', context)

  return redirect('index')
