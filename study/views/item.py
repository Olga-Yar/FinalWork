from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from study.models.item import Item
from study.paginators import ItemPaginator
from study.permissions import IsModerator
from study.seriallizers.item import ItemSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_permissions(self):
        """Проверка разрешения для различных методов"""
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions_classes = [IsModerator]  # создавать, удалять или обновлять может только модератор
        else:
            permissions_classes = [IsAuthenticated]  # остальные действия только для авторизованных пользователей

        return [permission() for permission in permissions_classes]

    def list(self, request, **kwargs):
        """Отображение списка разделов"""
        queryset = Item.objects.all()
        paginator = ItemPaginator()
        page = paginator.paginate_queryset(queryset, request)
        serializer = ItemSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение одного раздела"""
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Удаление раздела по PK"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
