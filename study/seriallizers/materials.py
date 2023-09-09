from rest_framework import serializers

from study.models.materials import Materials


class MaterialsSerializer(serializers.ModelSerializer):
    count_questions = serializers.SerializerMethodField()
    percent_complete = serializers.FloatField()
    question_title = serializers.SerializerMethodField()

    def get_count_questions(self, obj):
        """Расчет количества вопросов в данном материале"""
        return obj.question.all().count()

    def get_right_answers(self, obj):
        """Расчет количества правильных вопросов"""
        return obj.answers.count()

    def get_percent_complete(self, obj):
        """Расчет процента завершенности"""
        count_questions = obj.question.all().count()
        count_right_answers = obj.answers.filter(is_user_correct=True).count()
        if count_questions > 0:
            return count_right_answers / count_questions * 100
        return 0

    def get_question_title(self, obj):
        question = obj.question.all().values_list('title', flat=True)
        return list(question)

    class Meta:
        model = Materials
        fields = [
            'pk', 'name_m', 'question_title', 'is_finished', 'count_questions', 'percent_complete',
        ]
