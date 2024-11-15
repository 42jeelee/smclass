from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.
def stu_list(request):
  qs = Student.objects.all()

  context = {'list': qs}

  return render(request, 'stu_list.html', context)

def stu_write(request):
  return render(request, 'stu_write.html')

def stu_save(request):
  if request.method == 'POST':
    name = request.POST['s_name']
    major = request.POST['s_major']
    grade = request.POST['s_grade']
    age = request.POST['s_age']
    gender = request.POST['s_gender']

    qs = Student(s_name=name, s_major=major, s_grade=grade, s_age=age, s_gender=gender)
    qs.save()

  return redirect('students:stu_list')
