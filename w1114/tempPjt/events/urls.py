from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
  path('', views.eventView, name='reg')
]
