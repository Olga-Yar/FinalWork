from drf_yasg.inspectors import view
from rest_framework import status, request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from study.models.answers import Answers
from study.permissions import IsModerator
from study.seriallizers.answers import AnswersSerializer


class AnswersViewSet(ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

    # def get_permissions(self):
    #     """Проверка разрешения для различных методов"""
    #     if self.action == 'update' and self.action == 'partial_update':
    #         permissions_classes = [IsAuthenticated]  # остальные действия только для авторизованных пользователей
    #     elif self.action == 'create' or self.action == 'update' or self.action == 'destroy':
    #         permissions_classes = [IsModerator]  # создавать, удалять или обновлять может только модератор
    #     else:
    #         permissions_classes = [IsAuthenticated]  # остальные действия только для авторизованных пользователей
    #
    #     return [permission() for permission in permissions_classes]

    def list(self, request, **kwargs):
        """Отображение списка ответов"""
        queryset = Answers.objects.all()
        serializer = AnswersSerializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """Изменение пользователем только поля user_answer"""
        partial = kwargs.pop('partial', True)
        instance = self.get_object()

        if request.user.has_perm('study.change_answers'):
            if 'user_answer' in request.data:
                serializer = self.get_serializer(instance, data=request.data, partial=partial)
                serializer.is_valid(raise_exeption=True)

                serializer.save(user_answer=request.data['user_answer'])
                self.perform_update(serializer)
            else:
                return Response({'error': 'Можно изменить только поле ответ пользователя (user_answer)'},
                                status=status.HTTP_400_BAD_REQUEST)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

                return Response(serializer.data)

            return Response(status=status.HTTP_403_FORBIDDEN)


