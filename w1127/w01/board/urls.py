from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.blist, name='blist'),
    path('bwrite/', views.bwrite, name='bwrite'),
    path('bview/<str:bno>/', views.bview, name='bview'),
    path('bupdate/<str:bno>/', views.bupdate, name='bupdate'),
    path('bdelete/<str:bno>/', views.bdelete, name='bdelete'),
]
