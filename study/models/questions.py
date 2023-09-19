
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Question(models.Model):
    title = models.TextField(max_length=255, verbose_name='вопрос')
    is_active = models.BooleanField(default=True, verbose_name='опубликован')
    is_finished = models.BooleanField(default=False, verbose_name='завершено')
    answer = models.ManyToManyField('Answers')

    def __str__(self):
        return f'{self.title}: {self.is_active}, {self.is_finished}'

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
