from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views import generic
from django.urls import reverse_lazy
class TaskCreateView(generic.CreateView):
    model = models.Task
    template_name = "todo_app/todo_list.html"
    form_class = forms.TaskForm
    success_url = reverse_lazy('list')
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = models.Task.objects.all()
        return context
class TaskUpdateView(generic.UpdateView):
    model = models.Task
    template_name = "todo_app/todo_update.html"
    form_class = forms.TaskForm
    success_url = reverse_lazy('list')
class TaskDeleteView(generic.DeleteView):
    model = models.Task
    template_name = "todo_app/todo_delete.html"
    success_url = reverse_lazy('list')



