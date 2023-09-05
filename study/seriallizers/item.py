from rest_framework import serializers

from study.models.item import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'name', 'about', 'materials', 'user',
            ]
