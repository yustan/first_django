from asyncio import Task
from django.contrib import admin
from .models import Task
# Register your models here.
#зарегистрируем таблицу

admin.site.register(Task)