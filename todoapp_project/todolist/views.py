from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from .models import Task
import json
from django.http import JsonResponse

def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(author = request.user)
        return render(request, 'todoapp/home.html', {'taskList':tasks})
    
    return redirect('login')

def about(request):
    return render(request, "todoapp/about.html")

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'todoapp/home.html'
    context_object_name = 'taskList'
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskCreateView(CreateView):
    model = Task
    fields = ['content']
    success_url = reverse_lazy('todo-home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('todo-home')
    
def reorder_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        for index, taskId in enumerate(data['ids']):
            Task.objects.filter(id=taskId).update(order=index)
        return JsonResponse({'status':'ok'})
    
    