from django.shortcuts import render, redirect

# Create your views here.
def blist(request):
  return render(request, 'blist.html')

def bwrite(request):
  return render(request, 'bwrite.html')

def bview(request, bno):
  return render(request, 'bview.html')

def bupdate(request, bno):
  return render(request, 'bupdate.html')

def bdelete(request, bno):
  return redirect("index")