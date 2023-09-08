from django.urls import path
from rest_framework import routers

from study.apps import StudyConfig
from study.views.item import ItemViewSet

app_name = StudyConfig.name

urlpatterns = [
    path('item/', ItemViewSet.as_view({'get': 'list'})),
    path('item/<int:pk>/', ItemViewSet.as_view({'get': 'retrieve'})),
    path('item/<int:pk>/update/', ItemViewSet.as_view({'put': 'update'})),  # доступ только для модератора
    path('item/create/', ItemViewSet.as_view({'put': 'create'})),   # доступ только для модератора
]

router = routers.SimpleRouter()
router.register('habit', ItemViewSet)

urlpatterns += router.urls
