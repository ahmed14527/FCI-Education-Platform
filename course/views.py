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
    permission_classes = [AllowAny]

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class CreateCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]



class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

class CreateTagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    

class PrerequisiteListAPIView(generics.ListAPIView):
    queryset = Prerequisite.objects.all()
    serializer_class = PrerequisiteSerializer
    permission_classes = [AllowAny]

class CreatePrerequisiteViewSet(viewsets.ModelViewSet):
    queryset = Prerequisite.objects.all()
    serializer_class = PrerequisiteSerializer
    permission_classes = [AllowAny]
    


class LearningListAPIView(generics.ListAPIView):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer

class CreateLearningViewSet(viewsets.ModelViewSet):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer
    permission_classes = [IsAdminUser]



class UserCourseListAPIView(generics.ListAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


class CreateUserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    
    


class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CreateVideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUser]
    


    
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Course

def user_profile(request):
    user = request.user
    #courses = Course.objects.filter(usercourse__user=user)

    #course_list = []
    #for course in courses:
     #   course_data = {
      #      'id': course.id,
       ##     'name': course.name,
         #   'description': course.description,
          #  'discount': course.discount,
           # 'active': course.active,
            #'thumbnail': course.thumbnail.url,
      #      #'date': course.date,
       #     'resource': course.resource.url,
        #    'length': course.length,
            # Add more fields as needed
        #}
        #course_list.append(course_data)

    data = {
        'id': user.id,
        'username': user.username,
        #'courses': course_list,
    }
    return JsonResponse(data)
    
    
