from django.shortcuts import render, redirect
from member.models import Member
from django.http import JsonResponse

# Create your views here.
def loginChk(request):

  id = request.POST.get("id", "")
  pw = request.POST.get("pw", "")

  members = Member.objects.filter(id=id, pw=pw)

  if len(members) > 0:
    request.session['session_id'] = id
    request.session['session_nicName'] = members[0].nicName

    result = "success"
  else:
    result = "fail"

  context = {"result": result}
  return JsonResponse(context)

def login(request):
  return render(request, 'login.html')

def logout(request):
  request.session.clear()
  return redirect("member:login")

def step03(request):
  if request.method == "GET":
    return render(request, 'step03.html')
  
  id = request.POST.get('id')
  pw = request.POST.get('pw')

  return redirect("member:login")