from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import Taskform
from django.utils import timezone
from django.urls import reverse

from .tasks import add

def home(request):
    tasks = Task.objects
    flag = False
    return render(request, 'home/home.html', {'tasks': tasks.order_by('-pub_date'), 'flag':flag})

def search(request):
    if request.method == 'POST':
        searchquery = request.POST['searchquery']
        tasks = Task.objects.filter(title__contains=searchquery)
        return render(request, 'home/home.html', {'tasks': tasks.order_by('-pub_date')})

def asynch(request):

    if request.method == 'POST':
        input_1 = request.POST['input_1']
        input_2 = request.POST['input_2']
        try:
            result = add(input_1, input_2)
            return render(request, 'home/home.html', {'tasks': Task.objects.all().order_by('-pub_date'), 'input_1':input_1, 'input_2':input_2, 'result':result} )
        except:
            return render(request, 'home/home.html', {'tasks': Task.objects.all().order_by('-pub_date'), 'error':'please enter two numbers'} )
    else:
        return render(request, 'home/home.html', {'tasks': tasks.order_by('-pub_date')})

def hide(request):
    tasks = Task.objects
    flag = True
    return render(request, 'home/home.html', {'tasks': tasks.order_by('-pub_date').filter(completed=False), 'flag':flag})

def taskdetail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'home/taskdetail.html', {'task':task})

@login_required
def create(request):

    form = Taskform(request.POST or None)

    if form.is_valid():
        task = form.save(commit=False)
        task.pub_date = timezone.datetime.now()
        task.user = request.user
        form.save()
        return redirect('home')

    return render(request, 'home/create.html', {'form': form})

@login_required
def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    form = Taskform(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'home/edit.html', {'form': form, 'task':task})

@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return redirect('home')

@login_required
def markcompleted(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True if task.completed == False else False
    task.save()
    return redirect('home')
