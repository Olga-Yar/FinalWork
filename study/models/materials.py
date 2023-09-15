from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class Materials(models.Model):

    name_m = models.CharField(max_length=50, verbose_name='название')
    question = models.ManyToManyField('Question')
    is_finished = models.BooleanField(default=False, verbose_name='завершен')
    count_questions = models.IntegerField(verbose_name='количество вопросов', default=0)
    percent_complete = models.FloatField(verbose_name='процент выполнения', default=0.0)

    def __str__(self):
        return f'{self.name_m}: {self.percent_complete}'

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

    def save(self, *args, **kwargs):
        """Валидация названия на уровне модели"""
        if not self.name_m.isalpha() or not self.name_m.isascii() or not self.name_m.islower():
            raise ValidationError(
                _('Имя раздела должно содержать только русские буквы и быть в нижнем регистре.'),
                code='invalid_russian_name',
            )

        if not self.name_m[0].isupper():
            raise ValidationError(
                _('Имя раздела должно начинаться с заглавной буквы.'),
                code='invalid_starts_with_capital',
            )
