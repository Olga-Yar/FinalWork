from rest_framework import serializers

from user.models import UserCustom


class UserCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCustom
        fields = [
            'email', 'first_name', 'last_name', 'avatar', 'role',
        ]


# class CreateUserSerializer(serializers.ModelSerializer):
#     """Создание пользователя"""
#     class Meta:
#         model = UserCustom
#         fields = ['email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}
#
#         def create(self, validated_data):
#             user = UserCustom(
#                 email=validated_data['email']
#             )
#             user.set_password(validated_data['password'])
#             user.save()
#             return user
