from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from .models import Course, Tag, Prerequisite, Learning, UserCourse, Video, Category
from rest_framework.permissions import AllowAny
from django.views.generic import DetailView
from .models import Course
from .serializers import CourseSerializer, CourseDetailSerializer,CategoryDetailSerializer,VideoDetailSerializer,UserCourseDetailSerializer
from .serializers import (
    CourseSerializer,
    CategorySerializer,
    UserCourseSerializer,
    VideoSerializer,
)

class CreateCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    
class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'pk'

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class CreateCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]



class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'pk'


class UserCourseListAPIView(generics.ListAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


class CreateUserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    
    
class UserCourseDetailAPIView(generics.RetrieveAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseDetailSerializer
    lookup_field = 'pk'
    


class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CreateVideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    

class VideoDetailAPIView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer
    lookup_field = 'pk'
    
