
from django import forms
from tasks.models.task import Task

from tasks.models.user import User
# from pkg_resources import require

class TaskForm(forms.Form):
    title = forms.CharField(max_length=200,label='Titulo', widget=forms.TextInput(attrs={'class':'form-control'}),label_suffix=' ')
    user = forms.IntegerField(widget=forms.Select(attrs={'class':'form-control'}), label='Usuario',label_suffix=' ')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Description')
  
    class Meta:
        model = Task
        fields = ['title', 'user','description']

    
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.Select(choices=User.objects.all().values_list('id', 'name'), attrs={'class':'form-control'})
    

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == '':
            raise forms.ValidationError('El titulo es requerido')
        return title


    def clean_description(self):
        description = self.cleaned_data['description']
        if description == '':
            raise forms.ValidationError('La descripcion es requerida')
        return description

class UserForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}),label_suffix=' ')
    email = forms.EmailField(max_length=200, label='Email', widget=forms.TextInput(attrs={'class':'form-control'}),label_suffix=' ')
    telefono = forms.CharField(max_length=200, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}),label_suffix=' ')
    class Meta:
        model = User
        fields = ['name', 'email', 'telefono']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == '':
            raise forms.ValidationError('El nombre es requerido')
        return name
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('El email es requerido')
        return email
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono == '':
            raise forms.ValidationError('El telefono es requerido')
        return telefono
        