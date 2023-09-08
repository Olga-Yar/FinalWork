from rest_framework import serializers

from study.models.questions import Questions


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            'pk', 'title', 'is_active', 'is_finished',
        ]
