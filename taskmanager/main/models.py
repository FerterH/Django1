from django.db import models



class Task(models.Model):
    title = models.CharField('Название задачи', max_length=20)
    task = models.TextField('Подробное описание задачи')
    priority = models.TextField('Приоритет')

    def __str__(self):
        return self.title
