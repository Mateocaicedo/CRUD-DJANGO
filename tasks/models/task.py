from django.db import models

from . import user

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user.User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
