from django.urls import path, include
from rest_framework import routers
from .views import SheetViewSet, SheetListAPIView

router = routers.DefaultRouter()
router.register(r'create_sheets', SheetViewSet)

urlpatterns = [
    path('sheet/', SheetListAPIView.as_view(), name='sheet-list'),
    path('', include(router.urls)),
]