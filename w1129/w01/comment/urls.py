from django.urls import path
from . import views

app_name = 'comment'
urlpatterns = [
    path('clist/', views.clist, name='clist'),
    path('cwrite/', views.cwrite, name='cwrite'),
    path('cupdate/', views.cupdate, name='cupdate'),
    path('cdelete/', views.cdelete, name='cdelete'),
]
