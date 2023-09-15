import django_filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from study.models.materials import Materials
from study.permissions import IsModerator
from study.seriallizers.materials import MaterialsSerializer


class MaterialsViewSet(ModelViewSet):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = [IsAuthenticated | IsModerator]

    def list(self, request, **kwargs):
        """Отображение списка материалов"""
        queryset = Materials.objects.all()
        serializer = MaterialsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        """Отображение одного материала"""
        queryset = Materials.objects.all()
        material = get_object_or_404(queryset, pk=pk)
        serializer = MaterialsSerializer(material)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Удаление материала по PK"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
