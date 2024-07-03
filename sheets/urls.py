from django.urls import path, include
from rest_framework import routers
from .views import SheetsViewSet, SheetsListAPIView

router = routers.DefaultRouter()
router.register(r'create_sheets', SheetsViewSet)

urlpatterns = [
    path('sheet/', SheetsListAPIView.as_view(), name='sheet-list'),
    path('', include(router.urls)),
]