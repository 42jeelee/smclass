from django.shortcuts import render
from board.models import Board
from comment.models import Comment

# Create your views here.
def bview(request, bno):
  boards = Board.objects.filter(bno=bno)

  if len(boards) > 0:
    board = boards[0]
    comments = Comment.objects.filter(board=board)

    context = {"board": board, "clist": comments}
    return render(request, 'bview.html', context)

  context = {"emsg": "1"}
  return render(request, 'blist.html', context)

def blist(request):
  boards = Board.objects.all().order_by("-bgroup", "bstep")

  context = {"blist": boards}

  return render(request, 'blist.html', context)
