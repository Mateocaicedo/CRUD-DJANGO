from django.contrib import admin
from .models.task import Task
from .models.user import User

# Register your models here.


admin.site.register(Task)
admin.site.register(User)