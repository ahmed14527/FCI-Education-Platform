from django.contrib import admin
from .models import Category, Course, Tag, Prerequisite, Learning, UserCourse, Video

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'length', 'active']
    list_filter = ['category', 'active']
    search_fields = ['name', 'description']

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'serial_number', 'is_preview']
    list_filter = ['course', 'is_preview']
    search_fields = ['title', 'course__name']

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tag)
admin.site.register(Prerequisite)
admin.site.register(Learning)
admin.site.register(UserCourse)
admin.site.register(Video, VideoAdmin)