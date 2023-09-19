from rest_framework import status

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.models import UserCustom
from user.seriallizers import UserCustomSerializer


class UserCustomViewSet(ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer
    # permission_classes = [IsAuthenticated, IsModerator]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = UserCustom.objects.create_user(email=email, password=password)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
