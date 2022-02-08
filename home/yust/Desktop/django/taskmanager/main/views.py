from distutils.log import error
import re
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# При обращении мейн находится в темлейтс /taskmanager/main/TEMPLATES/main/
def index(request):
#    tasks = Task.objects.all()
    tasks = Task.objects.order_by('-article_date')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def create(request):
    error = ''
# Если передаются данные методом пост (кнопка добавить), значит мы их получаем form = TaskForm(request.POST), 
# далее проверяем if form.is_valid(): и сохраняем form.save() в базу данных, и редиректит на страницу home
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            error = 'Форма заполнена неверно'
# пересенная form которая представляет объект созданный на основе класса TaskForm (forms.py)
    form = TaskForm()
    contex = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', contex)


def about(request):
    return render(request, 'main/about.html')