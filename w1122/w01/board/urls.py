from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.blist, name='blist'),
    path('bwrite/', views.bwrite, name='bwrite'),
    path('bview/<int:bno>', views.bview, name='bview'),
    path('bmodify/<int:bno>', views.bmodify, name='bmodify'),
]
