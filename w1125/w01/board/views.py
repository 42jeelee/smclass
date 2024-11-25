from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import F

# Create your views here.
def breply(request, bno):
  if request.method == "GET":
    board = Board.objects.get(bno=bno)

    context = {"board": board}

    return render(request, 'breply.html', context)
  
  id = request.POST.get("id")
  member = Member.objects.get(id=id)

  btitle = request.POST.get("btitle")
  bcontent = request.POST.get("bcontent")
  bgroup = int(request.POST.get("bgroup"))
  bstep = int(request.POST.get("bstep"))
  bindent = int(request.POST.get("bindent"))

  query = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
  query.update(bstep=F('bstep') + 1)

  board = Board.objects.create(btitle=btitle, bcontent=bcontent, member=member, bgroup=bgroup, bstep=bstep + 1, bindent=bindent + 1)

  board.save()

  context = {"rmsg": "1"}
  return render(request, "breply.html", context)

def bupdate(request, bno):
  if request.method == "GET":
    board = Board.objects.get(bno=bno)

    context = {"board": board}

    return render(request, 'bupdate.html', context)
  
  btitle = request.POST.get("btitle")
  bcontent = request.POST.get("bcontent")

  board = Board.objects.get(bno=bno)
  board.btitle = btitle
  board.bcontent = bcontent

  board.save()

  return redirect("board:bview", bno)

def bdelete(request, bno):
  board = Board.objects.get(bno=bno)

  board.delete()
  context = {"dmsg": bno}
  return render(request, 'blist.html', context)


def bview(request, bno):
  board = Board.objects.get(bno=bno)

  context = {"board": board}

  response = render(request, 'bview.html', context)

  tomorrow = datetime.replace(datetime.now(), hour=23, minute=59, second=0)
  expires = datetime.strftime(tomorrow, '%a,%d=%b-%Y %H:%M:%S GMT')

  # prev_board = Board.objects.filter().order_by('-bgroup', 'bstep').first()
  # next_board = Board.objects.filter().order_by('bgroup', '-bstep').first()

  cName = request.COOKIES.get('cookie_name')
  if cName is not None:
    cName_list = cName.split("|")
    if str(bno) not in cName_list:
      board.bhit += 1
      board.save()

      response.set_cookie('cookie_name', cName + f"|{bno}", expires=expires)
  else:

    board.bhit += 1
    board.save()

    response.set_cookie('cookie_name', bno, expires=expires)

  return response

def bwrite(request):
  if request.method == "GET":
    return render(request, 'bwrite.html')
  
  id = request.session.get('session_id')
  member = Member.objects.get(id=id)

  btitle = request.POST.get('btitle')
  bcontent = request.POST.get('bcontent')
  bimg = request.FILES.get('bfile', '')

  board = Board.objects.create(btitle=btitle, bcontent=bcontent, member=member, bimg=bimg)
  board.bgroup = board.bno
  board.save()

  context = {"wmsg": "1"}
  return render(request, 'bwrite.html', context)

def blist(request):
  boards = Board.objects.all().order_by('-bgroup', 'bstep')

  context = {"blist": boards}

  return render(request, 'blist.html', context)