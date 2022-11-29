from django.contrib import messages

from django.shortcuts import redirect, render

from tasks.forms import *
from tasks.models.user import User
from tasks.models.task import Task
from tasks.views.user.user import users

def listTasks(request):
    allTasks = Task.objects.all().order_by("-created_at")

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
  
    if request.method == "POST":
        user =User.objects.get(id=request.POST['user'])  
        task = Task(title=request.POST['title'], description=request.POST['description'], user=user)
       
        form = TaskForm(
            request.POST,
        )

        if form.is_valid():
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Tarea creada correctamente')
            return redirect('list-tasks')
        else:
            return render(request, 'tasks/create-task.html', {
                'form': form
            })
      

def updateTask(request, id):


    task = Task.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'tasks/update-task.html', {
            'form': TaskForm(
                initial={
                    'title': task.title,
                    'description': task.description,
                    'user': task.user.id
                }
            )
        })

    if request.method == "POST":
        form = TaskForm(
            request.POST
        )

        if form.is_valid():
            task.title = request.POST['title']
            task.description = request.POST['description']
            task.user = User.objects.get(id=request.POST['user'])
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Tarea actualizada correctamente')
            return redirect('list-tasks')
        else:
            return render(request, 'tasks/update-task.html', {
                'form': form
            })
    
  

def completeTask(request, id):
    task = Task.objects.get(id=id)
    task.complete = True
    task.save()
    return redirect('list-tasks')