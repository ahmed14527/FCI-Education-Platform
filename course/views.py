from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Course, Tag, Prerequisite, Learning, UserCourse, Video, Category
from .serializers import (
    CourseSerializer,
    CategorySerializer,
    TagSerializer,
    PrerequisiteSerializer,
    LearningSerializer,
    UserCourseSerializer,
    VideoSerializer,
)

class CreateCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
@method_decorator(login_required, name='dispatch')
class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CreateCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer




class CreateTagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class PrerequisiteListAPIView(generics.ListAPIView):
    queryset = Prerequisite.objects.all()
    serializer_class = PrerequisiteSerializer

class CreatePrerequisiteViewSet(viewsets.ModelViewSet):
    queryset = Prerequisite.objects.all()
    serializer_class = PrerequisiteSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class LearningListAPIView(generics.ListAPIView):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer

class CreateLearningViewSet(viewsets.ModelViewSet):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class UserCourseListAPIView(generics.ListAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


@method_decorator(login_required, name='dispatch')
class CreateUserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


@method_decorator(login_required, name='dispatch')
class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CreateVideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUser]