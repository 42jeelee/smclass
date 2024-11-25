from django.shortcuts import render, redirect
from member.models import Member

# Create your views here.
def logout(request):
  request.session.clear()
  return redirect("/")

def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  
  id = request.POST.get('id')
  pw = request.POST.get('pw')

  members = Member.objects.filter(id=id, pw=pw)

  if len(members) > 0:
    context = {"lmsg": "1"}
    member = members[0]
    request.session['session_id'] = id
    request.session['session_nicName'] = member.nicName
  else:
    context = {"lmsg": "0"}

  return render(request, 'login.html', context)
