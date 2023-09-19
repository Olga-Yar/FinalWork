
from django.db import models
from rest_framework.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
import re


NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):

    name = models.CharField(max_length=50, verbose_name='раздел', unique=True)
    about = models.TextField(max_length=500, verbose_name='описание')
    materials = models.ManyToManyField('Materials')
    user = models.ManyToManyField('user.UserCustom')

    def __str__(self):
        return f'{self.name}: {self.about}'

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'

    def save(self, *args, **kwargs):
        """Валидация имени на уровне модели"""
        if not re.match("^[а-яА-Я]+$", self.name):
            raise ValidationError(
                _('Имя раздела должно содержать только русские буквы.'),
                code='invalid_russian_name',
            )

        if not self.name[0].isupper():
            raise ValidationError(
                _('Имя раздела должно начинаться с заглавной буквы.'),
                code='invalid_starts_with_capital',
            )

        super().save(*args, **kwargs)
