from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from study.models.answers import Answers
from study.seriallizers.answers import AnswersSerializer


class AnswersViewSet(ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, **kwargs):
        """Отображение списка ответов"""
        queryset = Answers.objects.all()
        serializer = AnswersSerializer(queryset, many=True)
        return Response(serializer.data)

