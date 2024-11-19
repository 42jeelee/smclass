from django.shortcuts import render, redirect
from students.models import Student
from django.urls import reverse

# Create your views here.
def trans_student(s):
  trans_hobbys = {"game":"게임", "golf":"골프", "swim":"수영", "run":"조깅"}

  s.gender = '남' if s.gender == 'M' else '여'
  s.hobbys = ', '.join([ trans_hobbys.get(h, h) for h in s.hobbys.split(',') ])

  return s


def list(request):
  students = Student.objects.all()

  return render(request, 'list.html', {"students": students})

def write(request):
  if request.method == 'POST':
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    hobbys = ','.join(request.POST.getlist('hobby'))

    student = Student(name=name, major=major, grade=grade, age=age, gender=gender, hobbys=hobbys)
    student.save()
    return redirect(reverse('students:view', kwargs={"id": student.id}))
  return render(request, 'write.html')

def view(request, id):
  students = Student.objects.filter(id=id)

  if len(students) == 1:
    student = trans_student(students[0])

    return render(request, 'view.html', {"student": student})
  
  return redirect('students:list')

def update(request, id):
  students = Student.objects.filter(id=id)

  if len(students) == 1:
    if request.method == 'POST':
      student = trans_student(students[0])
      
      student.major = request.POST['major']
      student.grade = request.POST['grade']
      student.age = request.POST['age']
      student.gender = request.POST['gender']
      student.hobbys = ','.join(request.POST.getlist('hobby'))

      student.save()

      return redirect(reverse('students:view', kwargs={"id": id}))
    elif request.method == 'GET':
      student = students[0]

      student.hobbys = student.hobbys.split(',')

      return render(request, 'update.html', {"student": student})
  
  return redirect('students:list')

def delete(request, id):
  students = Student.objects.filter(id=id)

  if len(students) == 1:
    students[0].delete()
  return redirect('students:list')