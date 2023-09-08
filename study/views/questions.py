from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from study.models.questions import Questions
from study.permissions import IsModerator
from study.seriallizers.questions import QuestionsSerializer


class QuestionsViewSet(ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = [IsAuthenticated | IsModerator]

    def list(self, request, **kwargs):
        """Отображение списка вопросов"""
        queryset = Questions.objects.all()
        serializer = QuestionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение одного вопроса"""
        queryset = Questions.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionsSerializer(question)
        return Response(serializer.data)
