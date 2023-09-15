from rest_framework import serializers

from user.models import UserCustom


class UserCustomSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserCustom
        fields = [
            'email', 'first_name', 'last_name', 'avatar', 'password', 'role',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserCustom.objects.create_user(password=password, **validated_data)
        return user


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
