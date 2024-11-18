from django.shortcuts import render, redirect
from students.models import Student

# Create your views here.
def list(request):
  students = Student.objects.all()
  context = {'students': students}

  return render(request, 'list.html', context)

def view(request, name):
  students = Student.objects.filter(name=name)

  if len(students) == 0:
    return redirect('students:list')

  return render(request, 'view.html', {'student': students[0]})

def write(request):
  if request.method == 'POST':
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']

    qs = Student(name=name, major=major, grade=grade, age=age, gender=gender)
    qs.save()

    return redirect('students:list')
  return render(request, 'write.html')


def modify(request, name):
  students = Student.objects.filter(name=name)

  if len(students) > 0:
    student = students[0]
    if request.method == 'GET':
      return render(request, 'update.html', {'student': student})
    elif request.method == 'POST':
      student.name = request.POST['name']
      student.major = request.POST['major']
      student.grade = request.POST['grade']
      student.age = request.POST['age']
      student.gender = request.POST['gender']

      student.save()

  return redirect("students:list")

def delete(request, name):
  students = Student.objects.filter(name=name)

  if len(students) > 0:
    student = students[0]

    student.delete()

  return redirect("students:list")