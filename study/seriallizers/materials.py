from rest_framework import serializers

from study.models.materials import Materials


class MaterialsSerializer(serializers.ModelSerializer):
    count_questions = serializers.SerializerMethodField()
    count_right_answers = serializers.SerializerMethodField()
    # answer = serializers.SerializerMethodField()
    percent_complete = serializers.FloatField()

    def get_count_questions(self, obj):
        """Расчет количества вопросов в данном материале"""
        return obj.questions.all().count()

    def get_questions(self, obj):
        """Список вопросов в материале"""
        return [i.pk for i in obj.questions.all()]

    def get_right_answers(self, obj):
        """Расчет количества правильных вопросов"""
        mistakes = 0
        rights = 0

        for answer in obj.answers.all():
            if answer.user_answer and answer.is_correct_answer is False:
                mistakes += 1
            elif answer.user_answer and answer.is_correct_answer:
                rights += 1
            elif answer.user_answer is False and answer.is_correct_answer:
                mistakes += 1

        total = mistakes + rights
        return rights

    def to_representation(self, instance):
        """Вычисление процента выполнения блока. В расчете учитываются только правильные ответа пользователя"""
        representation = super().to_representation(instance)
        representation['percent_complete'] = (
                representation['count_right_answers'] /
                representation['count_questions'] * 100
        )
        return representation

    class Meta:
        model = Materials
        fields = [
            'pk', 'name_m', 'questions', 'is_finished', 'count_questions', 'count_right_answers', 'percent_complete',
        ]
