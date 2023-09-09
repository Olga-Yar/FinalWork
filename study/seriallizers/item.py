from rest_framework import serializers

from study.models.item import Item
from study.seriallizers.materials import MaterialsSerializer


class ItemSerializer(serializers.ModelSerializer):
    materials_name = serializers.SerializerMethodField()

    def get_materials_name(self, obj):
        materials = obj.materials.all().values_list('name_m', flat=True)
        return list(materials)

    class Meta:
        model = Item
        fields = [
            'name', 'about', 'materials_name',
            ]
