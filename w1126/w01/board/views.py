from django.shortcuts import render
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import Q, F
from django.core.paginator import Paginator

# Create your views here.
def blist(request):
  npage = int(request.GET.get("npage", 1))
  boards = Board.objects.all().order_by("-bgroup", "bstep")

  paginator = Paginator(boards, 10)
  blist = paginator.get_page(npage)

  context = {"blist": blist, "npage": npage}

  return render(request, 'blist.html', context)

def breply(request, bno):
  board = Board.objects.get(bno=bno)
  if request.method == "GET":
    context = {"board": board}

    return render(request, 'breply.html', context)

  id = request.session.get('session_id')
  member = Member.objects.get(id=id)

  bgroup = int(request.POST.get("bgroup"))
  bstep = int(request.POST.get("bstep"))
  bindent = int(request.POST.get("bindent"))

  btitle = request.POST.get("btitle")
  bcontent = request.POST.get("bcontent")
  bfile = request.FILES.get("bfile", "")

  prev_replys = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
  prev_replys.update(bstep=F('bstep') + 1)

  reply_board = Board.objects.create(btitle=btitle, bcontent=bcontent, bfile=bfile, member=member, bgroup=bgroup, bstep=bstep+1, bindent=bindent+1)
  reply_board.save()

  context = {"rmsg": reply_board.bno}
  return render(request, 'breply.html', context)

def bdelete(request, bno):
  Board.objects.get(bno=bno).delete()

  context = {"dmsg": bno}
  return render(request, 'blist.html', context)

def bupdate(request, bno):
  board = Board.objects.get(bno=bno)
  if request.method == "GET":
    context = {"board": board}

    return render(request, 'bupdate.html', context)

  btitle = request.POST.get("btitle")
  bcontent = request.POST.get("bcontent")
  bfile = request.FILES.get("bfile", "")

  board.btitle = btitle
  board.bcontent = bcontent
  board.bfile = bfile if bfile != "" else board.bfile
  board.save()

  context = {"wmsg": "1"}
  return render(request, 'bupdate.html', context)

def bview(request, bno):
  npage = request.GET.get('npage', 1)
  board = Board.objects.get(bno=bno)

  prev_boards = Board.objects.filter(Q(bgroup__lt=board.bgroup, bstep__lte=board.bstep) | Q(bgroup=board.bgroup, bstep__gt=board.bstep)).order_by("-bgroup", "bstep")
  prev_board = prev_boards[0] if len(prev_boards) else None
  
  next_boards = Board.objects.filter(Q(bgroup__gt=board.bgroup, bstep__gte=board.bstep) | Q(bgroup=board.bgroup, bstep__lt=board.bstep)).order_by("bgroup", "-bstep")
  next_board = next_boards[0] if len(next_boards) else None

  context = {"board": board, "prev": prev_board, "next": next_board, "npage": npage}

  day1 = datetime.replace(datetime.now(), hour=23, minute=59, second=0)
  expires = datetime.strftime(day1, "%a, %d-%b-%Y %H:%M:S GMT")

  response = render(request, 'bview.html', context)

  cookie = request.COOKIES.get("cookie_boardNo")
  if cookie is not None:
    cookie_list = cookie.split("|")

    if str(bno) not in cookie_list:
      board.bhit += 1
      board.save()

      response.set_cookie("cookie_boardNo", cookie + f"|{bno}", expires=expires)
  else:
    board.bhit += 1
    board.save()

    response.set_cookie("cookie_boardNo", bno)

  return response

def bwrite(request):
  if request.method == "GET":
    return render(request, 'bwrite.html')
  
  id = request.session.get("session_id")
  member = Member.objects.get(id=id)

  btitle = request.POST.get("btitle")
  bcontent = request.POST.get("bcontent")
  bfile = request.FILES.get("bfile", "")

  board = Board.objects.create(btitle=btitle, member=member, bcontent=bcontent, bfile=bfile)
  board.bgroup = board.bno
  board.save()

  context = {"wmsg": "1"}
  return render(request, 'bwrite.html', context)
