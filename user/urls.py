
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

from user.apps import UserConfig
from user.views import UserCustomViewSet

app_name = UserConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenObtainPairView.as_view()),
    path('create/', UserCustomViewSet.as_view({'put': 'create'})),

]