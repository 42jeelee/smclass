from django.shortcuts import render
from django.http import JsonResponse
from member.models import Member
from django.core import serializers

# Create your views here.
def idChk(request):

  id = request.POST.get('id')

  members = Member.objects.filter(id=id)
  result = "success" if len(members) == 0 else "fail"

  context = {"result": result}
  return JsonResponse(context)

def step03(request):
  if request.method == "GET":
    return render(request, 'step03.html')
  
  return render(request, 'step03.html')

def logout(request):
  request.session.clear()

  context = {"outmsg": "1"}

  return render(request, 'index.html', context)

def loginChk(request):
  id = request.POST.get("id", "")
  pw = request.POST.get("pw", "")

  members = Member.objects.filter(id=id, pw=pw)
  if len(members):
    member = members[0]
    json_member = serializers.serialize('json', [member])

    request.session['session_id'] = id
    request.session['session_nicName'] = member.nicName

    context = {"result": "success", "member": json_member}
  else:
    context = {"result": "fail"}

  return JsonResponse(context)

def login(request):
  return render(request, 'login.html')