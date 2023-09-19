from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from study.models.questions import Question


class QuestionSerializer(serializers.ModelSerializer):
    answer_name = SerializerMethodField()
    answer_pk = SerializerMethodField()

    def get_answer_name(self, obj):
        answer = obj.answer.all().values_list('answer', flat=True)
        return list(answer)

    def get_answer_pk(self, obj):
        ans_pk = obj.answer.all().values_list('pk', flat=True)
        return list(ans_pk)

    class Meta:
        model = Question
        fields = [
            'pk', 'title', 'answer_pk', 'answer_name', 'is_active', 'is_finished',
        ]
