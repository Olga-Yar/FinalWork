from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Materials(models.Model):

    name = models.CharField(max_length=50, verbose_name='название', **NULLABLE)
    item = models.ForeignKey('Item', on_delete=models.SET_NULL, verbose_name='раздел', **NULLABLE) # при удалении - какую зависимость?
    tests = models.ManyToManyField('Tests', on_delete=models.SET_NULL, verbose_name='тест', **NULLABLE) # при удалении - какую зависимость?
    completed = models.IntegerField(verbose_name='доля выполненного', default=0) # будет расчет

    def __str__(self):
        return f'{self.name}: {self.completed}'

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
