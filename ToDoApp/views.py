from django.shortcuts import render
from datetime import date
import calendar
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import RegistrationForm, TaskCreateForm
from .models import Person, Task
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, TemplateView, LogoutView


# Create your views here.

class MainView(TemplateView):
    template_name = 'ToDoApp/main.html'


class PersonRegistration(CreateView):
    template_name = 'ToDoApp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('ToDoApp:main')

class PersonLogin(LoginView):
    template_name = 'ToDoApp/login.html'

    def get_redirect_url(self):
        return '/todoproject/task_detail/'


class TaskCreateView(CreateView):
    template_name = 'ToDoApp/create_task.html'
    form_class = TaskCreateForm
    success_url = '/todoproject/task_detail/'

    def form_valid(self, form):

        task = form.instance
        user = self.request.user
        person = Person.objects.filter(username=user)
        person = person[0]
        task.person = person
        task.save()
        self.object = task
        return HttpResponseRedirect(self.get_success_url())


class TaskList(ListView):
    model = Task

    def get_queryset(self):
        user = self.request.user
        user = Person.objects.filter(username=user)
        user = user[0]
        task = Task.objects.filter(person=user)
        return task

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        my_date = date.today()
        today = calendar.day_name[my_date.weekday()]
        context = {
            'paginator' : None,
            'page_obj' : None,
            'is_paginated' : False,
            'object_list' : self.object_list,
            'my_date' : my_date,
            'today' : today
        }
        return self.render_to_response(context)


class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'ToDoApp/update_task.html'
    fields = ['task_title', 'task_description', 'task_category']
    success_url = reverse_lazy('ToDoApp:task_detail')


class DeleteTaskView(DeleteView):
    template_name = 'ToDoApp/delete_task.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('ToDoApp:task_detail')


class LogOut(LogoutView):
    next_page = '/todoproject/'