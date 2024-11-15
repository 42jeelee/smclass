from django.contrib import admin
from students.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
  list_display = ['s_name', 's_major', 's_age']

admin.site.register(Student, StudentAdmin)
