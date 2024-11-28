from django.shortcuts import render
from comment.models import Comment
from board.models import Board
from member.models import Member
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def cwrite(request):
  id = request.session.get('session_id')
  member = Member.objects.get(id=id)
  
  bno = request.POST.get("bno", 1)
  board = Board.objects.get(bno=bno)
  
  cpw = request.POST.get("cpw", "")
  ccontent = request.POST.get("ccontent", "")

  comment = Comment.objects.create(board=board, member=member, cpw=cpw, ccontent=ccontent)
  comment.save()

  json_comment = serializers.serialize('json', [comment])

  context = {"comment": json_comment, "result": "success"}
  return JsonResponse(context)