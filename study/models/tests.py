from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Tests(models.Model):
    test = models.CharField()
    materials = models.ForeignKey('Materials', verbose_name='материал')
    time_for_complete = models.TimeField()
    time_start = models.TimeField(auto_now=True, verbose_name='время начала')
    is_finished = models.BooleanField(default=False, verbose_name='завершен')
    correct_answer = models.CharField(verbose_name='верный ответ')

    def __str__(self):
        return f'{self.pk}: {self.is_finished}'

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'
