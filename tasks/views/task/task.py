from django.shortcuts import redirect, render

from tasks.forms import *
from tasks.models.user import User
from tasks.models.task import Task

def listTasks(request):
    allTasks = Task.objects.all().order_by("-created_at")
    for t in allTasks:
        print(t)
    return render(request, 'tasks/tasks.html', {
        'tasks': allTasks
    })


def deleteTask(request, id):
    t = Task.objects.get(id=id)
    t.delete()
    return redirect('list-tasks')


def createTask(request):
    if request.method == "GET":
        return render(request, 'tasks/create-task.html', {
            'form': TaskForm()
        })

    t = TaskForm(request.POST)
    if  t.is_valid() == False:
        return render(request, 'tasks/create-task.html', {
            'form': t
        })
    
    task = Task()
    task.title = request.POST['title']
    task.description = request.POST['description']
    task.user = User.objects.get(id=request.POST['user'])
    task.save()
    return redirect('list-tasks')
    

def updateTask(request, id):
    task = Task.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'tasks/update-task.html', {
            'form': TaskForm(instance = task)
        })

    task.title = request.POST['title']
    task.description = request.POST['description']
    task.user = User.objects.get(id=request.POST['user'])
    task.save()
    return redirect('list-tasks')