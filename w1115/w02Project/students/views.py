from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

# Create your views here.

## 학생 전체 리스트 호출
def stu_list(request):
  # 학생 전체 리스트 가져오기
  qs = Student.objects.all()

  # 정보 전달 변수 생성
  context = {"list": qs}
  return render(request, 'stu_list.html', context)

## 학생 입력 페이지 호출
def write(request):
  return render(request, 'stu_write.html')

## 학생 입력 저장
def save(request):
  print('학생 정보 저장 호출')
  if request.method == 'POST':
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']

    print(name, major, grade, age, gender)

    qs = Student(s_name=name, s_major=major, s_grade=grade, s_age=age, s_gender=gender)
    qs.save()
    
  return redirect('index')
  # return redirect(reverse('index')) # reverse : app_name
  # return HttpResponseRedirect(reverse('index'))

