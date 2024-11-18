from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.
def list(request):
  students = Student.objects.all()

  return render(request, {'students': students})


def write(request):
  if request.method == 'POST':
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']

    student = Student(name=name, major=major, grade=grade, age=age, gender=gender)
    student.save()

    return redirect('/')
  
  return render(request, 'write.html')


def sView(request, name):
  students = Student.objects.filter(name=name)

  if len(students) > 0:
    return render(request, 'sView.html', {'student': students[0]})
  
  return redirect('/')
