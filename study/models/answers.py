from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Answers(models.Model):
    answer = models.CharField(max_length=150, verbose_name='ответ')
    user_answer = models.BooleanField(default=False, verbose_name='ответ пользователя')
    is_correct_answer = models.BooleanField(default=False, verbose_name='правильный ответ')
    is_user_correct = models.BooleanField(default=False, verbose_name='верный ли ответ пользователя')

    def __str__(self):
        return f'{self.answer} - {self.is_correct_answer}, {self.user_answer}'

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'

    def save(self, *args, **kwargs):
        """Проверка ответа пользователя"""
        if self.user_answer and self.is_correct_answer:
            self.is_user_correct = True
        else:
            self.is_user_correct = False


