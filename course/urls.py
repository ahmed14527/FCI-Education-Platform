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
    #CourseUpdateAPIView ,
    CourseDeleteAPIView,
    #CategoryUpdateAPIView,
    #CategoryDeleteAPIView,
    #TagUpdateAPIView,
    #TagDeleteAPIView,
    #PrerequisiteUpdateAPIView,
    #PrerequisiteDeleteAPIView,
    #LearningUpdateAPIView,
    #LearningDeleteAPIView,
    #UserCourseUpdateAPIView
    #,UserCourseDeleteAPIView
    #,VideoUpdateAPIView,
    #VideoDeleteAPIView
    
    
    
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
    #path('api/courses/<int:pk>/', CourseUpdateAPIView.as_view(), name='course-update'),
    #path('api/courses/<int:pk>/', CourseDeleteAPIView.as_view(), name='course-delete'),
    #path('categories/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    #path('categories/<int:pk>/delete/', CategoryDeleteAPIView.as_view(), name='category-delete'),
    #path('tags/<int:pk>/', TagUpdateAPIView.as_view(), name='tag-update'),
    #path('tags/<int:pk>/delete/', TagDeleteAPIView.as_view(), name='tag-delete'),
    #path('prerequisites/<int:pk>/', PrerequisiteUpdateAPIView.as_view(), name='prerequisite-update'),
    #path('prerequisites/<int:pk>/delete/', PrerequisiteDeleteAPIView.as_view(), name='prerequisite-delete'),    
    #path('learnings/<int:pk>/', LearningUpdateAPIView.as_view(), name='learning-update'),
    #path('learnings/<int:pk>/delete/', LearningDeleteAPIView.as_view(), name='learning-delete'),    
    #path('usercourses/<int:pk>/', UserCourseUpdateAPIView.as_view(), name='user-course-update'),
    #path('usercourses/<int:pk>/delete/', UserCourseDeleteAPIView.as_view(), name='user-course-delete'),    
    #path('videos/<int:pk>/', VideoUpdateAPIView.as_view(), name='video-update'),
    #path('videos/<int:pk>/delete/', VideoDeleteAPIView.as_view(), name='video-delete'),
    path('', include(router.urls)),
]