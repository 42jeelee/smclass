from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.list, name='list'),
    path('write', views.write, name='write'),
    path('<str:id>', views.view, name='view'),
    path('<str:id>/update', views.update, name='update'),
    path('<str:id>/delete', views.delete, name='delete'),
]
