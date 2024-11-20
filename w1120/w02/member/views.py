from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def logout(request):
  request.session.clear() # 세션 모두 삭제
  # del request.session['session_id'] # 해당 세션만 삭제
  return redirect('/')

def login(request):
  if request.method == 'GET':
    response = render(request, 'login.html')
  else:
    emsg = ""
    id = request.POST.get("id")
    pw = request.POST.get("pw")

    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      qs = qs[0]
      context = {"emsg": emsg, "member": qs}
      response = render(request, 'index.html', context)
    else:
      emsg = "아이디 또는 패스워드가 일치하지 않습니다."
      context = {"emsg": emsg, "member": ""}
      response = render(request, 'login.html', context)


  return response


def cookDelete(request):
  if request.method == 'GET':
    response = render(request, 'cookDelete.html')
  else:
    response = render(request, 'index.html')
    c = request.POST.get('ckey')

    response.delete_cookie(c)
  return response

def cookWrite(request):
  if request.method == 'GET':
    response = render(request, 'cookWrite.html')
  
    return response
  else:
    response = render(request, 'index.html')
    ckey = request.POST.get('ckey')
    cvalue = request.POST.get('cvalue')

    response.set_cookie(ckey, cvalue)

    return response


def mlist(request):
  return render(request, 'mlist.html')

