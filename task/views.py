from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)

def update(request, pk):
    particular_task = Task.objects.get(id=pk)
    form = TaskForm(instance=particular_task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=particular_task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'update.html', context={'form': form})

def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'delete.html', context={'item': item})