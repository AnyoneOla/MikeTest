from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import User_Request
from .forms import TaskForm

from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView


def thanks(request):
    return render(request, 'tasks/user_request_thanks.html')

class TaskListView(ListView):
    model = User_Request
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = User_Request

class TaskCreateView(CreateView):
    model = User_Request
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_thanks')

class TaskUpdateView(UpdateView):
    model = User_Request
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(DeleteView):
    model = User_Request
    success_url = reverse_lazy('tasks:task_list')
