from django.urls import path
from rest_framework import routers
from .views import (
    NotificationViewSet,
    NotificationListAPIView,
    ReminderViewSet,
    ReminderListAPIView,
)

router = routers.DefaultRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('api/notifications/', NotificationListAPIView.as_view(), name='notification-list'),
    path('api/reminders/', ReminderListAPIView.as_view(), name='reminder-list'),
]

urlpatterns += router.urls