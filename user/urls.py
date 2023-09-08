
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from django.urls import path, include

from user.apps import UserConfig
from user.views import UserCustomViewSet

app_name = UserConfig.name

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenObtainPairView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('create/', UserCustomViewSet.as_view({'put': 'create'})),

]