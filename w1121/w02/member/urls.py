from django.urls import path
from . import views

app_name = "member"
urlpatterns = [
    path('join1/', views.join1, name='join1'),
    path('join2/', views.join2, name='join2'),
    path('join3/', views.join3, name='join3'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
