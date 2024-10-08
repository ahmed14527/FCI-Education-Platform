from django.urls import path
from rest_framework import routers
from .views import (
    CreateCategoryViewSet,
    CategoryListAPIView,
    CourseListAPIView,
    CreateCourseViewSet,
    UserCourseListAPIView,
    CreateUserCourseViewSet,
    VideoListAPIView,
    CreateVideoViewSet,
)
from . import views

router = routers.DefaultRouter()
router.register(r'categories', CreateCategoryViewSet)
router.register(r'courses', CreateCourseViewSet)
router.register(r'courses', CreateUserCourseViewSet)
router.register(r'videos', CreateVideoViewSet)

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    #path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),
    path('course/', CourseListAPIView.as_view(), name='course-list'),
    #path('courses/<int:pk>/', views.CourseDetailAPIView.as_view(), name='course-detail'),    
    path('user-course/', UserCourseListAPIView.as_view(), name='user-course-list'),
    #path('user-courses/<int:pk>/', views.UserCourseDetailAPIView.as_view(), name='user-course-detail'),
    path('video/', VideoListAPIView.as_view(), name='video-list'),
    #path('videos/<int:pk>/', views.VideoDetailAPIView.as_view(), name='video-detail'),

]+router.urls

