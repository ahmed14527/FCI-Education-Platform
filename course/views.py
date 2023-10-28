from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Course, Tag, Prerequisite, Learning, UserCourse, Video, Category
from .serializers import (
    CourseSerializer,
    CategorySerializer,
    CreateCategorySerializer,
    TagSerializer,
    PrerequisiteSerializer,
    LearningSerializer,
    UserCourseSerializer,
    VideoSerializer,
    CreateCourseSerializer,
    CreateLearningSerializer,
    CreatePrerequisiteSerializer,
    CreateTagSerializer,
    CreateUserCourseSerializer,
    CreateVideoSerializer,
)

@method_decorator(login_required, name='dispatch')
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CreateCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CreateTagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class PrerequisiteViewSet(viewsets.ModelViewSet):
    queryset = Prerequisite.objects.all()
    serializer_class = PrerequisiteSerializer


class CreatePrerequisiteViewSet(viewsets.ModelViewSet):
    queryset = Prerequisite.objects.all()
    serializer_class = CreatePrerequisiteSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class LearningViewSet(viewsets.ModelViewSet):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer


class CreateLearningViewSet(viewsets.ModelViewSet):
    queryset = Learning.objects.all()
    serializer_class = CreateLearningSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class UserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


@method_decorator(login_required, name='dispatch')
class CreateUserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = CreateUserCourseSerializer


@method_decorator(login_required, name='dispatch')
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CreateVideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = CreateVideoSerializer
    permission_classes = [IsAdminUser]