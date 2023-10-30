from django.urls import path, include
from rest_framework import routers
from .views import  SheetViewSet

router = routers.DefaultRouter()
router.register(r'sheets', SheetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]