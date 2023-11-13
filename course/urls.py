from django.urls import path
from rest_framework import routers
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
    user_profile,
)

router = routers.DefaultRouter()
router.register(r'categories', CreateCategoryViewSet)
router.register(r'courses', CreateCourseViewSet)
router.register(r'tags', CreateTagViewSet)
router.register(r'prerequisites', CreatePrerequisiteViewSet)
router.register(r'learnings', CreateLearningViewSet)
router.register(r'user-courses', CreateUserCourseViewSet)
router.register(r'videos', CreateVideoViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('prerequisites/', PrerequisiteListAPIView.as_view(), name='prerequisite-list'),
    path('learnings/', LearningListAPIView.as_view(), name='learning-list'),
    path('user-courses/', UserCourseListAPIView.as_view(), name='user-course-list'),
    path('videos/', VideoListAPIView.as_view(), name='video-list'),
    path('user-profile/', user_profile, name='user-profile'),
]

urlpatterns += router.urls