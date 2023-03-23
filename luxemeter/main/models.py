from django.db import models



class Task(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Пленки'
