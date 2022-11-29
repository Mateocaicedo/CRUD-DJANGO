from django.contrib import messages
from django.shortcuts import redirect, render
from tasks.forms import *
from tasks.models.user import User
from django.core.paginator import Paginator

def users(request):
    allUsers = User.objects.all().order_by("-created_at")
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(allUsers, 10)
        users = paginator.page(page)
    except: 
        users = paginator.page(paginator.num_pages)

    return render(request, 'users/users.html', {
        'instance': users,
        'paginator': paginator
        })
   


def createUser(request):
    if request.method == "GET":
        return render(request, 'users/create-user.html', {
            'form': UserForm()
        })

    u = UserForm(request.POST)
    if  u.is_valid():
        u.save()
        messages.add_message(request, messages.SUCCESS, 'Usuario creado correctamente')
        return redirect('list-users')
    else:
        return render(request, 'users/create-user.html', {
            'form': u
        })



def deleteUser(request, id):
    u = User.objects.get(id=id)
    u.delete()
    messages.add_message(request, messages.ERROR, 'Usuario eliminado correctamente')
    return redirect('list-users')

def updateUser(request, id):
    u = User.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'users/update-user.html', {
            'form': UserForm(
                initial={
                    'name': u.name,
                    'email': u.email,
                    'telefono': u.telefono,
                }
            )
        })

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            u.name = request.POST['name']
            u.email = request.POST['email']
            u.telefono = request.POST['telefono']
            u.save()
            messages.add_message(request, messages.SUCCESS, 'Usuario actualizado correctamente')
            return redirect('list-users')
        else:
            return render(request, 'users/update-user.html', {
                'form': form
            })
   
