from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
  path('', views.stu_list, name='stu_list'),
  path('save/', views.stu_save, name='stu_save'),
  path('write/', views.stu_write, name='stu_write'),
]