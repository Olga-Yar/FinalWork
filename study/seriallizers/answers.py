from rest_framework import serializers

from study.models.answers import Answers


class AnswersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Answers
        fields = [
            'question', 'answer', 'user_answer', 'is_correct_answer', 'is_user_correct', 'user',
        ]
