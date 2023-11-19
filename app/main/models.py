from django.db import models

class Task(models.Model):
    title = models.CharField('Назавание', max_length=50)
    tasks = models.TextField('Задача')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
# Create your models here.
class Task_add(models.Model):
    title_add = models.CharField('Назавание', max_length=50)
    tasks_add = models.TextField('Задача')

    def __str__(self):
        return self.title_add