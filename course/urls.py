from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,
    CreateCategoryViewSet,
    CourseViewSet,
    CreateCourseViewSet,
    TagViewSet,
    CreateTagViewSet,
    PrerequisiteViewSet,
    CreatePrerequisiteViewSet,
    LearningViewSet,
    CreateLearningViewSet,
    UserCourseViewSet,
    CreateUserCourseViewSet,
    VideoViewSet,
    CreateVideoViewSet,
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'create-categories', CreateCategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'create-courses', CreateCourseViewSet)
router.register(r'tags', TagViewSet)
router.register(r'create-tags', CreateTagViewSet)
router.register(r'prerequisites', PrerequisiteViewSet)
router.register(r'create-prerequisites', CreatePrerequisiteViewSet)
router.register(r'learnings', LearningViewSet)
router.register(r'create-learnings', CreateLearningViewSet)
router.register(r'user-courses', UserCourseViewSet)
router.register(r'create-user-courses', CreateUserCourseViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'create-videos', CreateVideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]