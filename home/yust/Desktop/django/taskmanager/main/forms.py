from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
#для объединения поля title и task в нарисованную
#Добавляем аттрибуты к полям созданным {{ form.title }} {{ form.task }}
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание задачи'
            })
        }

