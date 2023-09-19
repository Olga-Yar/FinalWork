from rest_framework import serializers

from study.models.materials import Materials


class MaterialsSerializer(serializers.ModelSerializer):
    count_questions = serializers.SerializerMethodField()
    # percent_complete = serializers.FloatField()
    question_title = serializers.SerializerMethodField()
    question_pk = serializers.SerializerMethodField()
    # count_is_user_correct = serializers.SerializerMethodField()

    def get_count_questions(self, obj):
        """Расчет количества вопросов в данном материале"""
        return obj.question.all().count()

    # def get_count_is_user_correct(self, obj):
    #     """Расчет количества правильный ответов пользователя"""
    #     return obj.question.filter(answer__is_user_correct=True).count()

    # def get_percent_complete(self, obj):
    #     """Расчет процента завершенности"""
    #     if self.count_questions > 0:
    #         self.percent_complete = self.count_is_user_correct / self.count_questions * 100
    #     else:
    #         self.percent_complete = 0.0
    #     return self.percent_complete

    def get_question_title(self, obj):
        """Получение названия вопросов"""
        question = obj.question.all().values_list('title', flat=True)
        return list(question)

    def get_question_pk(self, obj):
        """Получения РК вопросов"""
        que_pk = obj.question.all().values_list('pk', flat=True)
        return que_pk

    class Meta:
        model = Materials
        fields = [
            'pk', 'name_m', 'question_pk', 'question_title', 'is_finished', 'count_questions',
        ]
