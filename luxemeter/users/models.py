from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

