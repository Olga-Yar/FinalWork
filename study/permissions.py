
from rest_framework.permissions import BasePermission

from user.models import UserRoles


class IsModerator(BasePermission):
    message = 'Доступ закрыт!'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False
