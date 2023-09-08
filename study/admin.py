from django.contrib import admin

from study.models.answers import Answers
from study.models.item import Item
from study.models.materials import Materials
from study.models.questions import Question


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'about',
    )


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name_m', 'is_finished', 'percent_complete',
    )
    list_filter = ('item__name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'is_active', 'is_finished',
    )
    list_filter = ('materials__name_m',)


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'answer', 'user_answer', 'is_correct_answer', 'is_user_correct'
    )
    list_filter = ('question__title',)
