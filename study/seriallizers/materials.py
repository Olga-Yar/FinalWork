from rest_framework import serializers

from study.models.materials import Materials


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = [
            'name', 'question', 'is_finished', 'count_questions', 'percent_complete',
        ]
