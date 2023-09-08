from django.urls import path
from rest_framework import routers

from study.apps import StudyConfig
from study.views.item import ItemViewSet
from study.views.materials import MaterialsViewSet
from study.views.questions import QuestionViewSet

app_name = StudyConfig.name

urlpatterns = [
    path('item/', ItemViewSet.as_view({'get': 'list'})),
    path('item/<int:pk>/', ItemViewSet.as_view({'get': 'retrieve'})),
    path('item/<int:pk>/update/', ItemViewSet.as_view({'put': 'update'})),  # доступ только для модератора
    path('item/create/', ItemViewSet.as_view({'put': 'create'})),   # доступ только для модератора

    path('materials/', MaterialsViewSet.as_view({'get': 'list'})),
    path('materials/<int:pk>/', MaterialsViewSet.as_view({'get': 'retrieve'})),
    path('materials/<int:pk>/update/', MaterialsViewSet.as_view({'put': 'update'})),  # доступ только для модератора
    path('materials/create/', MaterialsViewSet.as_view({'put': 'create'})),   # доступ только для модератора

    path('questions/', QuestionViewSet.as_view({'get': 'list'})),
    path('questions/<int:pk>/', QuestionViewSet.as_view({'get': 'retrieve'})),
    path('questions/<int:pk>/update/', QuestionViewSet.as_view({'put': 'update'})),  # доступ только для модератора
    path('questions/create/', QuestionViewSet.as_view({'put': 'create'})),   # доступ только для модератора
]

router = routers.SimpleRouter()
router.register('study', ItemViewSet)

urlpatterns += router.urls
