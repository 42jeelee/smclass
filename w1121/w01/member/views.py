from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def trans_hobby(hobbys):
  t_hobbys = {'game': '게임', 'golf': '골프', 'swim': '수영', 'run': '조깅'}

  return ', '.join([ t_hobbys.get(h, '') for h in hobbys.split(',') ])

def mdelete(request, id):
  member = Member.objects.filter(id=id)

  if len(member) > 0:
    member[0].delete()

  return redirect("member:mlist")

def mupdate(request, id):
  member = Member.objects.filter(id=id)

  if len(member) > 0:
    member = member[0]

    if request.method == 'GET':
      member.hobby = member.hobby.split(',')
      
      return render(request, 'mupdate.html', {'member': member})
    elif request.method == 'POST':
      member.pw = request.POST.get('pw')
      member.name = request.POST.get('name')
      member.nickname = request.POST.get('nickname')
      member.tel = request.POST.get('tel')
      member.gender = request.POST.get('gender')
      member.hobby = ','.join(request.POST.getlist('hobby'))

      member.save()
      return redirect("member:mview", id)

  return redirect("member:mlist")


def mview(request, id):
  member = Member.objects.filter(id=id)

  if len(member) > 0:
    member = member[0]

    member.hobby = trans_hobby(member.hobby)

    return render(request, 'mview.html', {'member': member})

  return redirect('member:mlist')

def mwrite(request):
  if request.method == 'GET':
    return render(request, 'mwrite.html')
  
  id = request.POST.get('id')
  pw = request.POST.get('pw')
  name = request.POST.get('name')
  nickname = request.POST.get('nickname')
  tel = request.POST.get('tel')
  gender = request.POST.get('gender')
  hobby = ",".join(request.POST.getlist('hobby'))
  
  member = Member(id=id, pw=pw, name=name, nickname=nickname, tel=tel, gender=gender, hobby=hobby)
  member.save()

  return redirect('member:mlist')

def mlist(request):
  members = Member.objects.all()
  return render(request, 'mlist.html', {'members': members})

def logout(request):
  request.session.clear()
  return redirect('index')

def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  id = request.POST.get('id')
  pw = request.POST.get('pw')

  qs = Member.objects.filter(id=id, pw=pw)
  if qs:
    msg = "로그인 되었습니다."
    
    request.session['session_id'] = id
    request.session['session_nickname'] = qs[0].nickname

    return redirect('index')
  else:
    msg = "아이디 또는 패스워드가 일치하지 않습니다."
    
  return render(request, 'login.html', {"msg": msg})
