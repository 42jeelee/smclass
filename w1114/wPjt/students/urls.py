from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register, name='register'),
    path('reg/submit/', views.submit, name='register'),
]
