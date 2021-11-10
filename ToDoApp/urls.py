
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = 'ToDoApp'

urlpatterns = [
    path('registration/', views.PersonRegistration.as_view(), name='registration'),
    path('create_task/', views.TaskCreateView.as_view(), name='create_task'),
    path('task_detail/', views.TaskList.as_view(), name='task_detail'),
    path('update_task/<int:pk>/', views.UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('login/', views.PersonLogin.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('', views.MainView.as_view(), name='main'),

]
