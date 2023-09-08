from rest_framework import serializers

from study.models.questions import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'pk', 'title', 'is_active', 'is_finished',
        ]
