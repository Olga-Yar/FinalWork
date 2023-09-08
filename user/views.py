from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from user.models import UserCustom
from user.seriallizers import UserCustomSerializer


class UserCustomViewSet(ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer
    # permission_classes = [IsAuthenticated, IsModerator]
