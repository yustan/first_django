from statistics import mode
from django.db import models
from django.urls import reverse

# отвечает за новую табличку в базе данных
class Task(models.Model):
    # табличка будет содержать два поля
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')
    article_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#    def get_absolute_url(self):
#        return reverse('article-detail', kwargs={'pk': self.pk})
    
# как будет отображаться название в панеле администратора 
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'