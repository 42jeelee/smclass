from django.shortcuts import render
from django.http import JsonResponse
from member.models import Member
from board.models import Board
from comment.models import Comment
from django.core import serializers

# Create your views here.
def clist(request):

  context = {"result": "fail"}
  return JsonResponse(context)

def cwrite(request):

  id = request.session['session_id']
  member = Member.objects.get(id=id)

  bno = request.POST.get("bno", "")
  board = Board.objects.get(bno=bno)
  
  ccontent = request.POST.get("ccontent", "")
  cpw = request.POST.get("cpw", "")

  comment = Comment.objects.create(member=member, board=board, ccontent=ccontent, cpw=cpw)

  json_comment = serializers.serialize('json', [comment])

  context = {"result": "success", "comment": json_comment}
  return JsonResponse(context)

def cupdate(request):
  cno = request.POST.get("cno", "")
  ccontent = request.POST.get("ccontent", "")
  cpw = request.POST.get("cpw", "")

  comment = Comment.objects.get(cno=cno)

  if comment.cpw == cpw:
    comment.ccontent = ccontent
    comment.save()

    result = "success"
  else:
    result = "password_error"

  context = {"result": result}
  return JsonResponse(context)


def cdelete(request):
  cno = request.POST.get("cno", "")

  comment = Comment.objects.get(cno=cno)
  comment.delete()

  context = {"result": "success"}
  return JsonResponse(context)