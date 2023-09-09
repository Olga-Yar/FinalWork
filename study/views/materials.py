import django_filters
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

    # def get_queryset(self):
    #     item_id = self.kwargs['item_id']
    #     return Materials.objects.filter(section=item_id)

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
