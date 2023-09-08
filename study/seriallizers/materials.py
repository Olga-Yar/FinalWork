from rest_framework import serializers

from study.models.materials import Materials


class MaterialsSerializer(serializers.ModelSerializer):
    count_questions = serializers.SerializerMethodField()
    # count_right_answers = serializers.SerializerMethodField()
    # answer = serializers.SerializerMethodField()
    percent_complete = serializers.FloatField()

    # def get_num_questions(self, obj):
    #     """Расчет количества вопросов в данном материале"""
    #     return obj.question.all().count()
    #
    # def get_question(self, obj):
    #     """Список вопросов в материале"""
    #     return [i.pk for i in obj.question.all()]
    #
    # def get_num_right_answers(self, obj):
    #     """Получение количества правильных ответов текущего пользователя в данном материале"""
    #     return obj.answers_set.filter(is_user_correct=True).count()
    #
    # def to_representation(self, instance):
    #     """Вычисление процента выполнения блока. В расчете учитываются только правильные ответа пользователя"""
    #     representation = super().to_representation(instance)
    #     representation['percent_complete'] = (
    #             representation['num_right_answers'] /
    #             representation['num_questions'] * 100
    #     )
    #     return representation

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


    class Meta:
        model = Materials
        fields = [
            'pk', 'name_m', 'question', 'is_finished', 'count_questions', 'percent_complete',
        ]
