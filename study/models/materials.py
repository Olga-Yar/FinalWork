from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Materials(models.Model):

    name = models.CharField(max_length=50, verbose_name='название', **NULLABLE)
    question = models.ForeignKey('Questions', on_delete=models.SET_NULL, **NULLABLE) # при удалении - какую зависимость?
    is_finished = models.BooleanField(default=False, verbose_name='завершен')
    count_questions = models.IntegerField(verbose_name='количество вопросов', default=0)
    percent_complete = models.FloatField(verbose_name='процент выполнения', default=0.0)

    def __str__(self):
        return f'{self.name}: {self.percent_complete}'

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
