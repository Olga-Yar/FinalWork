from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Questions(models.Model):
    title = models.TextField(max_length=255, verbose_name='вопрос', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='опубликован')
    time_start = models.TimeField(auto_now=True, verbose_name='время старта')
    time_for_complete = models.TimeField(default='00:01:00', verbose_name='время на выполнение')
    is_finished = models.BooleanField(default=False, verbose_name='завершено')

    def __str__(self):
        return f'{self.title}: {self.is_active}, {self.is_finished}'

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
