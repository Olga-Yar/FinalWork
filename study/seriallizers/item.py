from rest_framework import serializers

from study.models.item import Item


class ItemSerializer(serializers.ModelSerializer):
    materials_name = serializers.SerializerMethodField()
    materials_pk = serializers.SerializerMethodField()

    def get_materials_name(self, obj):
        materials = obj.materials.all().values_list('name_m', flat=True)
        return list(materials)

    def get_materials_pk(self, obj):
        mat_pk = obj.materials.all().values_list('pk', flat=True)
        return mat_pk

    class Meta:
        model = Item
        fields = [
            'pk', 'name', 'about', 'materials_pk', 'materials_name',
        ]
