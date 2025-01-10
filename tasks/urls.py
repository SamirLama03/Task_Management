from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('tasklist/', views.task_list, name="tasklist"),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'), 
]
