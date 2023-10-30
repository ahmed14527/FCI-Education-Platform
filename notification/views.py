from rest_framework import viewsets
from .models import Notification, Reminder
from .serializers import NotificationSerializer, ReminderSerializer
from rest_framework import generics

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
    
class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    
class ReminderListAPIView(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer