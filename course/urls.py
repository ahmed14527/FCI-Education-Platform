from django.urls import path, include
from rest_framework import routers
from .views import user_profile

from .views import (
    CreateCategoryViewSet,
    CategoryListAPIView,
    CourseListAPIView,
    CreateCourseViewSet,
    TagListAPIView,
    CreateTagViewSet,
    PrerequisiteListAPIView,
    CreatePrerequisiteViewSet,
    LearningListAPIView,
    CreateLearningViewSet,
    UserCourseListAPIView,
    CreateUserCourseViewSet,
    VideoListAPIView,
    CreateVideoViewSet,
)

router = routers.DefaultRouter()
router.register(r'create-categories', CreateCategoryViewSet)
router.register(r'create-courses', CreateCourseViewSet)
router.register(r'create-tags', CreateTagViewSet)
router.register(r'create-prerequisites', CreatePrerequisiteViewSet)
router.register(r'create-learnings', CreateLearningViewSet)
router.register(r'create-user-courses', CreateUserCourseViewSet)
router.register(r'create-videos', CreateVideoViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('prerequisites/', PrerequisiteListAPIView.as_view(), name='prerequisite-list'),
    path('learnings/', LearningListAPIView.as_view(), name='learning-list'),
    path('user-courses/', UserCourseListAPIView.as_view(), name='user-course-list'),
    path('videos/', VideoListAPIView.as_view(), name='video-list'),
    path('user-profile/', user_profile, name='user_profile'),
    path('', include(router.urls)),
]