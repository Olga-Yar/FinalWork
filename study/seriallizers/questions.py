from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from study.models.questions import Question
from study.seriallizers.answers import AnswersSerializer


class QuestionSerializer(serializers.ModelSerializer):
    answer_name = SerializerMethodField()

    def get_answer_name(self, obj):
        answer = obj.answer.all().values_list('answer', flat=True)
        return list(answer)

    class Meta:
        model = Question
        fields = [
            'pk', 'title', 'answer_name', 'is_active', 'is_finished',
        ]
