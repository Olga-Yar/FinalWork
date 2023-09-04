from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):

    name = models.CharField(max_length=50, verbose_name='раздел', **NULLABLE)
    about = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}: {self.about}'

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'
