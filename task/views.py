from django.shortcuts import render
from django.http import HttpResponse
from task.models import Task
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(task_manager=self.request.user)


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(CreateView):
    model = Task
    fields =['title','content']
    def form_valid(self,form):
        form.instance.task_manager = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Task
    fields =['title','content']
    def form_valid(self,form):
        form.instance.task_manager = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.task_manager

class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Task
    success_url = '/'
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.task_manager