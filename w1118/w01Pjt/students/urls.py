from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
  path('', views.list, name='list'),
  path('write/', views.write, name='write'),
  path('<str:name>/', views.view, name='view'),
  path('<str:name>/modify/', views.modify, name='modify'),
  path('<str:name>/delete/', views.delete, name='delete'),
]