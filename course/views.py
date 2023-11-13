from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
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

@login_required
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
#class CategoryUpdateAPIView(APIView):
   # def put(self, request, pk):
      #  category = Category.objects.get(pk=pk)
      #  serializer = CategorySerializer(category, data=request.data)
      #  if serializer.is_valid():
      #      serializer.save()
       #     return Response(serializer.data)
      #  return Response(serializer.errors, status=400)
    
    #permission_classes = [IsAdminUser]


#class CategoryDeleteAPIView(DestroyAPIView):
  #  queryset = Category.objects.all()
  #  serializer_class = CategorySerializer
   # permission_classes = [IsAdminUser]

    
    
@method_decorator(login_required, name='dispatch')
class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CreateCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]

##lass CourseUpdateAPIView(APIView):
   # def put(self, request, pk):
      #  course = Course.objects.get(pk=pk)
       # serializer = CourseSerializer(course, data=request.data)
       # if serializer.is_valid():
        #    serializer.save()
         #   return Response(serializer.data)
        #return Response(serializer.errors, status=400)
    #permission_classes = [IsAdminUser]

class CourseDeleteAPIView(DestroyAPIView):
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
    
#class TagUpdateAPIView(APIView):
   # def put(self, request, pk):
        #tag = Tag.objects.get(pk=pk)
       # serializer = TagSerializer(tag, data=request.data)
       # if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data)
        #return Response(serializer.errors, status=400)
    #permission_classes = [IsAdminUser]

#class TagDeleteAPIView(DestroyAPIView):
   # queryset = Tag.objects.all()
   # serializer_class = TagSerializer
   # permission_classes = [IsAdminUser]

@method_decorator(login_required, name='dispatch')
class PrerequisiteListAPIView(generics.ListAPIView):
    queryset = Prerequisite.objects.all()
    serializer_class = PrerequisiteSerializer

class CreatePrerequisiteViewSet(viewsets.ModelViewSet):
    queryset = Prerequisite.objects.all()
    serializer_class = PrerequisiteSerializer
    permission_classes = [IsAdminUser]
    
#class PrerequisiteUpdateAPIView(APIView):
 #   def put(self, request, pk):
    #    prerequisite = Prerequisite.objects.get(pk=pk)
     #   serializer = PrerequisiteSerializer(prerequisite, data=request.data)
     #   if serializer.is_valid():
     #       serializer.save()
     #       return Response(serializer.data)
     #   return Response(serializer.errors, status=400)
   # permission_classes = [IsAdminUser]

#class PrerequisiteDeleteAPIView(DestroyAPIView):
   # queryset = Prerequisite.objects.all()
   # serializer_class = PrerequisiteSerializer
   # permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class LearningListAPIView(generics.ListAPIView):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer

class CreateLearningViewSet(viewsets.ModelViewSet):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer
    permission_classes = [IsAdminUser]

#class LearningUpdateAPIView(APIView):
 #   def put(self, request, pk):
  #      learning = Learning.objects.get(pk=pk)
   #     serializer = Learning(learning, data=request.data)
    #    if serializer.is_valid():
     #       serializer.save()
      #      return Response(serializer.data)
       # return Response(serializer.errors, status=400)
    #permission_classes = [IsAdminUser]

#class LearningDeleteAPIView(DestroyAPIView):
 #   queryset = Learning.objects.all()
  #  serializer_class = LearningSerializer
   # permission_classes = [IsAdminUser]

@method_decorator(login_required, name='dispatch')
class UserCourseListAPIView(generics.ListAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer


@method_decorator(login_required, name='dispatch')
class CreateUserCourseViewSet(viewsets.ModelViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
    
    

#@method_decorator(login_required, name='dispatch')
#class UserCourseUpdateAPIView(APIView):
   # def put(self, request, pk):
       # userCourse = UserCourse.objects.get(pk=pk)
       # serializer = UserCourse(userCourse, data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data)
     #   return Response(serializer.errors, status=400)
    
    
#@method_decorator(login_required, name='dispatch')
#class UserCourseDeleteAPIView(DestroyAPIView):
    #queryset = UserCourse.objects.all()
   # serializer_class = UserCourseSerializer


@method_decorator(login_required, name='dispatch')
class VideoListAPIView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class CreateVideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAdminUser]
    
#class VideoUpdateAPIView(APIView):
  #  def put(self, request, pk):
     #   video = Video.objects.get(pk=pk)
      #  serializer = Video(video, data=request.data)
      #  if serializer.is_valid():
        #    serializer.save()
       #     return Response(serializer.data)
      #  return Response(serializer.errors, status=400)
    #permission_classes = [IsAdminUser]

#class VideoDeleteAPIView(DestroyAPIView):
   # queryset = Video.objects.all()
   # serializer_class = VideoSerializer
   # permission_classes = [IsAdminUser]

    
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Course

@login_required
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
    
    
