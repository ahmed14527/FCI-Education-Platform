from django.contrib import admin
from .models import Category, Course, Tag, Prerequisite, Learning, UserCourse, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'length', 'active', 'discount', 'date']
    list_filter = ['category', 'active', 'date']
    search_fields = ['name', 'description']
    list_editable = ['active', 'discount']
    date_hierarchy = 'date'
    readonly_fields = ['date']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['description', 'course']
    list_filter = ['course']


@admin.register(Prerequisite)
class PrerequisiteAdmin(admin.ModelAdmin):
    list_display = ['description', 'course']
    list_filter = ['course']


@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    list_display = ['description', 'course']
    list_filter = ['course']


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'date']
    list_filter = ['user', 'course', 'date']
    search_fields = ['user__username', 'course__name']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'video_id']
    list_filter = ['course']