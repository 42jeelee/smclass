from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
  path('', views.list, name='list'),
  path('write/', views.write, name='write'),
  path('<str:name>/', views.sView, name='sView'),
]
