from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventView, name='eventView'),
]
