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
    permission_classes = [IsAuthenticated | IsModerator]

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
