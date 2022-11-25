
from django.urls import path

from .views.home import index
from .views.task import task
from .views.user import user


urlpatterns = [
    path('', index, name='index'),
 
    path('tasks/', task.listTasks, name='list-tasks'),
    path('delete-task/<int:id>', task.deleteTask, name='delete-task'),
    path('create-task/', task.createTask, name='create-task'),
    path('update-task/<int:id>', task.updateTask, name='update-task'),

    path('create-user/',user.createUser, name='create-user'),
    path('users/', user.users, name='list-users'),
    path('delete-user/<int:id>', user.deleteUser, name='delete-user'),
    path('update-user/<int:id>', user.updateUser, name='update-user'),
]