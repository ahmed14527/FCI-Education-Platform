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
router.register(r'Create-categories', CreateCategoryViewSet)
router.register(r'Create-courses', CreateCourseViewSet)
router.register(r'Create-tags', CreateTagViewSet)
router.register(r'Create-prerequisites', CreatePrerequisiteViewSet)
router.register(r'Create-learnings', CreateLearningViewSet)
router.register(r'Create-user-courses', CreateUserCourseViewSet)
router.register(r'Create-videos', CreateVideoViewSet)

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('course/', CourseListAPIView.as_view(), name='course-list'),
    path('tag/', TagListAPIView.as_view(), name='tag-list'),
    path('prerequisite/', PrerequisiteListAPIView.as_view(), name='prerequisite-list'),
    path('learning/', LearningListAPIView.as_view(), name='learning-list'),
    path('user-course/', UserCourseListAPIView.as_view(), name='user-course-list'),
    path('video/', VideoListAPIView.as_view(), name='video-list'),
    path('user-profile/', user_profile, name='user-profile'),
]

urlpatterns += router.urls