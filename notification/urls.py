from django.urls import path, include
from rest_framework import routers
from .views import NotificationViewSet, ReminderViewSet

router = routers.DefaultRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]