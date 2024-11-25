from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import F
from board.models import Board

# Create your views here.
def bmodify(request, bno):
  boards = Board.objects.filter(bno=bno)

  if len(boards) > 0:
    board = boards[0]
    if request.method == "GET":
      return render(request, 'bmodify.html', {'board': board})

    board.btitle = request.POST.get('btitle')
    board.bcontent = request.POST.get('bcontent')

    board.save()
    messages.success(request, message="게시글이 수정되었습니다.")
    return redirect("board:bview", bno)

  return redirect("board:blist")

def bview(request, bno):

  boards = Board.objects.filter(bno=bno)

  boards.update(bhit=F('bhit') + 1)

  if len(boards) > 0:
    board = boards[0]

    # board.bhit += 1
    # board.save()

    context = {"board": board}

    return render(request, 'bview.html', context)

  return redirect("board:blist")

def bwrite(request):
  if request.method == "GET":
    return render(request, 'bwrite.html')
  
  id = request.POST.get("id")
  btitle = request.POST.get("btitle")
  bcontent = request.POST.get("bcontent")

  board = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
  board.bgroup = board.bno
  board.save()

  messages.success(request, message="게시글이 저장되었습니다.")

  return redirect("board:blist")

def blist(request):
  board = Board.objects.all().order_by("-bgroup", "bstep")
  context = {"board": board}
  return render(request, 'blist.html', context)