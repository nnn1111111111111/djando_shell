from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):


    class Meta:
        model = Task
        fields = ['title', 'tasks']
        widgets = {'title':TextInput(attrs={
            'class':'form-conrol',
            'placeholder':'Введите название'
            }),
            'tasks': Textarea(attrs={
                'class': 'form-conrol',
                'placeholder': 'Введите описание'
            })
        }