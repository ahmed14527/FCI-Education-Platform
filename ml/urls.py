from django.urls import path, include
from rest_framework import routers
from .views import MLViewSet, MLListAPIView

router = routers.DefaultRouter()
router.register(r'create_mlfile', MLViewSet)

urlpatterns = [
    path('mlfile/', MLListAPIView.as_view(), name='sheet-list'),
    path('', include(router.urls)),
]