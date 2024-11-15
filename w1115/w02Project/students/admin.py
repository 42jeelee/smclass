from django.contrib import admin
from students.models import Student

# Register your models here.

## admin 관리자 페이지에서 컬럼 보여지는 부분 설정
class StudentAdmin(admin.ModelAdmin):
  list_display = ['s_name', 's_major', 's_age']

## admin 사이트에 추가
admin.site.register(Student, StudentAdmin)