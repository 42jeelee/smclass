from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mlist/', views.mlist, name='mlist'),
    path('mview/<str:id>/', views.mview, name='mview'),
    path('mupdate/<str:id>/', views.mupdate, name='mupdate'),
    path('mdelete/<str:id>/', views.mdelete, name='mdelete'),
    path('mwrite/', views.mwrite, name='mwrite'),
]
