from django.urls import include, path
from rest_framework import routers
from .views import (
    CourseViewSet,
    TagViewSet,
    CategoryViewSet,
    PrerequisiteViewSet,
    LearningViewSet,
    UserCourseViewSet,
    VideoViewSet,
    CreateCourseViewSet,
    CreateTagViewSet,
    CreateCategoryViewSet,
    CreateUserCourseViewSet,
    CreateVideoViewSet,
    CreateLearningViewSet,
    CreatePrerequisiteViewSet,
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'create-category', CreateCategoryViewSet, basename='create-category')
router.register(r'courses', CourseViewSet)
router.register(r'create-course', CreateCourseViewSet, basename='create-course')
router.register(r'tags', TagViewSet)
router.register(r'create-tag', CreateTagViewSet, basename='create-tag')
router.register(r'prerequisites', PrerequisiteViewSet)
router.register(r'create-prerequisites', CreatePrerequisiteViewSet, basename='create-prerequisites')
router.register(r'learnings', LearningViewSet)
router.register(r'create-learnings', CreateLearningViewSet, basename='create-learnings')
router.register(r'user-courses', UserCourseViewSet)
router.register(r'create-user-course', CreateUserCourseViewSet, basename='create-user-course')
router.register(r'payments', PaymentViewSet)
router.register(r'create-payment', CreatePaymentViewSet, basename='create-payment')
router.register(r'videos', VideoViewSet)
router.register(r'create-videos', CreateVideoViewSet, basename='create-videos')


urlpatterns = [
    path('', include(router.urls)),
]