from django.shortcuts import render
from django.http import JsonResponse
from member.models import Member

# Create your views here.
def idChk(request):
  id = request.POST.get("id", "")

  member = Member.objects.filter(id=id)

  result = "success" if len(member) == 0 else "fail"
  
  context = {"result": result}

  return JsonResponse(context)

def join01(request):
  return render(request, 'join01.html')

def join02(request):
  return render(request, 'join02.html')

def join03(request):
  return render(request, 'join03.html')

def loginChk(request):
  id = request.POST.get("id", "")
  pw = request.POST.get("pw", "")
 
  members = Member.objects.filter(id=id, pw=pw)

  if len(members) > 0:
    member = members[0]
    context = {"id": id, "nicName": member.nicName, "result": "success"}
  else:
    context = {"result": "fail"}

  return JsonResponse(context)

def login(request):
  return render(request, 'login.html')
