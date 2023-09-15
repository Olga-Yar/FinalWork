from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

NULLABLE = {'blank': True, 'null': True}


class Materials(models.Model):

    name_m = models.CharField(max_length=50, verbose_name='название', **NULLABLE)
    question = models.ManyToManyField('Question')
    is_finished = models.BooleanField(default=False, verbose_name='завершен')
    count_questions = models.IntegerField(verbose_name='количество вопросов', default=0)
    percent_complete = models.FloatField(verbose_name='процент выполнения', default=0.0)

    def __str__(self):
        return f'{self.name_m}: {self.percent_complete}'

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

    # def save(self, *args, **kwargs):
    #     """Расчет процента завершенности"""
    #     self.count_questions = self.question.all().count()
    #     self.count_right_answers = self.answers.filter(is_user_correct=True).count()
    #     if self.count_questions > 0:
    #         self.percent_complete = self.count_right_answers / self.count_questions * 100
    #     else:
    #         self.percent_complete = 0.0
    #
    #     super().save(*args, **kwargs)
