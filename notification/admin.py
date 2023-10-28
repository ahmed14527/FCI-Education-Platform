from django.contrib import admin
from .models import Notification, Reminder

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')
    list_filter = ('user', 'is_read')
    search_fields = ('user__username', 'message')

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'due_date')
    list_filter = ('user',)
    search_fields = ('user__username', 'title', 'description')