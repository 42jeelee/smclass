from django.shortcuts import render, redirect

# Create your views here.
def register(request):
  return render(request, 'register.html')

def submit(request):
  if request.method == 'GET':
    req_data = request.data

    print(req_data)

  return redirect("/")