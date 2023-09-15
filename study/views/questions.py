import django_filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from study.models.questions import Question
from study.permissions import IsModerator
from study.seriallizers.questions import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('materials__name_m',)

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions_classes = [IsModerator]  # создавать, удалять или обновлять может только модератор
        else:
            permissions_classes = [IsAuthenticated]  # остальные действия только для авторизованных пользователей

        return [permission() for permission in permissions_classes]

    def list(self, request, **kwargs):
        """Отображение списка вопросов"""
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение одного вопроса"""
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Удаление вопроса по PK"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
