from django.shortcuts import redirect, render
from tasks.forms import *
from tasks.models.user import User


def users(request):
    allUsers = User.objects.all().order_by("-created_at")

    return render(request, 'users/users.html', {
        'users': allUsers
    })


def createUser(request):
    if request.method == "GET":
        return render(request, 'users/create-user.html', {
            'form': UserForm()
        })

    u = UserForm(request.POST)
    if  u.is_valid():
        u.save()
        return redirect('list-users')
    else:
        return render(request, 'users/create-user.html', {
            'form': u
        })



def deleteUser(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return redirect('list-users')

def updateUser(request, id):
    u = User.objects.get(id=id)
    form = UserForm(instance=u)

    if request.method == "GET":
        return render(request, 'users/update-user.html', {
            'form': form
        })

    u.name = request.POST['name']
    u.email = request.POST['email']
    u.telefono = request.POST['telefono']
    u.save()
    return redirect('list-users')