from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.models import Tasks
from todoapp.forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TaskListView(ListView):
    model = Tasks
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'details.html'
    context_object_name = 'tasks'

class TaskUpdateView(UpdateView):
    model = Tasks
    template_name = 'update.html'
    context_object_name = 'tasks'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')


# def index(request):
#     movie=Tasks.objects.all()
#     context={
#         'todo_list':movie
#     }
#     return render(request,'index.html',context)

def index(request):
    task = Tasks.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date', '')
        tasks=Tasks(name=name,priority=priority,date=date)
        tasks.save()
    return  render(request,'home.html',{'tasks':task})

def details(request):
    task=Tasks.objects.all()
    return  render(request,'details.html',{'tasks':task})

def delete(request,taskid):
    task=Tasks.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return  render(request,'delete.html')

def update(request,id):
    task=Tasks.objects.get(id=id)
    form=TaskForm(request.POST or None,request.FILES,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})