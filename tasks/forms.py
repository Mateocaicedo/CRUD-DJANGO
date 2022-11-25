from django import forms
from tasks.models.task import Task

from tasks.models.user import User
# from pkg_resources import require

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=200,label='Titulo', required=True)
    description = forms.CharField(widget=forms.Textarea, label='Description', required=False)
    user = forms.IntegerField()
    class Meta:
        model = Task
        fields = ['title', 'description', 'user']

    
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.Select(choices=User.objects.all().values_list('id', 'name'))

class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label='Nombre', required=True)
    email = forms.EmailField(max_length=200, label='Email', required=True)
    telefono = forms.CharField(max_length=200, label='Telefono', required=True)
    class Meta:
        model = User
        fields = ['name', 'email', 'telefono']

