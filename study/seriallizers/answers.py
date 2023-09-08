from rest_framework import serializers

from study.models.answers import Answers


class AnswersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_is_user_correct(self, obj):
        if obj.user_answer and obj.is_correct_answer:
            return True

    class Meta:
        model = Answers
        fields = [
            'question', 'answer', 'user_answer', 'is_correct_answer', 'is_user_correct', 'user',
        ]
