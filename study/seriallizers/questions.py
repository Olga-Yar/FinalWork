from rest_framework import serializers

from study.models.questions import Questions


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            'title', 'is_active', 'time_start', 'time_for_complete', 'is_finished',
        ]
