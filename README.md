


# Django--FCI-PLATFORM
<p>An online education platform developed in django-3 which allow users to learn online :) </p>

<img src="C:\Users\bin shawky\Downloads\WhatsApp Image 2024-02-18 at 4.57.40 PM.jpeg">

### Live App
* checkout the site here: <a href="https://fci-platform.onrender.com/" target="_blank" >Deployed App</a> (little note below)

(Note: The website can take upto 30 seconds (hosted on Render free tier services), as the project has no clients, its just for learning, please refer the source
code to run locally).

### Short Note

This guide will Step-by-Step help you to create your own online educayion platform application in django. React and Django Framework. 

Note: this guide is not for absolute beginners so im assuming that you have the basic knowledge of MVT in django to get started. To know more on it i recommend you <a href="https://docs.djangoproject.com/en/3.0/">django documentation</a>.

# Table of contents
- [About_this_App](#About_this_App)
- [Get_Started](#Get_Started)
- [course_app](#Course_App)
  * [models](#models)
  * [migrations](#migrations)
  * [admin](#admin)
  * [server](#server)
  * [views](#views)
  * [urls](#urls)
  
<hr>

## About_this_App
The objective of this website will Enhance the quality of learning and teaching. Meet the
learning style or needs of students. Improve the efficiency and effectiveness. Improve useraccessibility and time flexibility to engage learners in the learning process.
Our E-learning website is FCI-PLATFORM that will help you to learn online. And access free
courses
from our website.

## Get_Started

I'm assuming that you are already done with setting up virtual enviornment in your system. Ok, now lets move to a location where we can store this project by using terminal or command prompt in windows. In my case im at this location,

yash@yash-SVE15113ENB:~/Documents/django_project/$ 

* Now Setup the virtual environment

$`pipenv shell`

$`pipenv install django==3.0`

## course-app

Lets begin our project by starting our project and installing a books app, type below commands in terminal.

(django_project)$`django-admin startproject fciplatform .` (do not avoid this period)

(django_project)$`python manage.py startapp course`

Now, open your favourite IDE and locate this project directory. (Im using VS Code so it should be something like this) note that at this point django doesnt know about this app, therefore we need to mention this app name inside our settings.py file.

* settings.py 

open your ecom_project folder, in here you will find settings.py file (open it). Go to Installed app section and mention your app name there (as shown below).


	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',

	    # my apps,				# changes
	    'course',
	    ]


### models

When done with the settings.py file, open the course folder (our app), in here you we find models.py file (open it)
Now put the following code in it,


	from django.db import models
	from django.db import models
	from django.contrib.auth.models import User
	from django.conf import settings

	class Category(models.Model):
    	name = models.CharField(max_length=200)

    	def __str__(self):
        	return self.name
    
    
    
	class Course(models.Model):
    	category = models.ForeignKey(Category, on_delete=models.CASCADE)
    	name = models.CharField(max_length = 50 , null = False)
    	description = models.CharField(max_length = 200 , null = True)
    	discount = models.IntegerField(null=False , default = 0) 
    	active = models.BooleanField(default = False)
    	thumbnail = models.ImageField(upload_to='images/')
    	date = models.DateTimeField(auto_now_add= True) 
    	resource = models.FileField(upload_to='images/')
    	length = models.IntegerField(null=False)

    	def __str__(self):
        	return self.name
    

    
    
	class CourseProperty(models.Model):
    	description  = models.CharField(max_length = 100 , null = False)
    	course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)

    	class Meta : 
       	 	abstract = True


	class Tag(CourseProperty):
    	pass
    
	class Prerequisite(CourseProperty):
    	pass

	class Learning(CourseProperty):
    	pass


	class UserCourse(models.Model):
    	user = models.ForeignKey(User , null = False , on_delete=models.CASCADE)
    	course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    	date = models.DateTimeField(auto_now_add=True)


    	def __str__(self):
        	return f'{self.user.username} - {self.course.name}'
    
    



	class Video(models.Model):
    	title  = models.CharField(max_length = 100 , null = False)
    	serial_number = models.IntegerField(null=True, blank=True)
    	course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    	video_id = models.CharField(max_length = 100 , null = False)
    	video_file = models.FileField(upload_to='images/')
    	is_preview = models.BooleanField(default = False)

    	def __str__(self):
        	return self.title
    
    


    


* what we done here ?

I created a model named as 'category' working on default django model (models.Model), this model contains 1 fields. Why ? beacuse  we want to add name for each category , and we create course model that contain 9 fields that we want to add name and image and its category ,add usercourse that contain 3 fields , add video model that contain 5 fileds that is very important  . By setting it to True (course is available) .


## migrations 

now its time to create some tables in our database, most of which is already handled by django, we just need to run following commands:

(django_project)$`python manage.py makemigrations`

(django_project)$`python manage.py migrate`

simply, the migrations command tells us what changes are going to be made in our database (right now two models will be created one is course and other one is category ,video ,usercouse), the migrate command is just like conformation stage of makemigrations command (means if you agree with the changes mentioned by migrations command then in order to perform those changes we run migrate command) 

Note: its a quick illustration of these commands the depth knowledge is available in <a href="https://docs.djangoproject.com/en/3.0/topics/migrations/">django documentation</a>


### admin

now we need to register our models in admin file in order in to use them. Put the following code in admin.py file

	from django.contrib import admin
	from .models import Category, Course, Tag, Prerequisite, Learning, UserCourse, Video


	@admin.register(Category)
	class CategoryAdmin(admin.ModelAdmin):
    	list_display = ['name']


	@admin.register(Course)
	class CourseAdmin(admin.ModelAdmin):
    	list_display = ['name', 'category', 'length', 'active', 'discount', 'date']
    	list_filter = ['category', 'active', 'date']
    	search_fields = ['name', 'description']
    	list_editable = ['active', 'discount']
    	date_hierarchy = 'date'
    	readonly_fields = ['date']


	@admin.register(Tag)
	class TagAdmin(admin.ModelAdmin):
    	list_display = ['description', 'course']
    	list_filter = ['course']


	@admin.register(Prerequisite)
	class PrerequisiteAdmin(admin.ModelAdmin):
    	list_display = ['description', 'course']
    l	ist_filter = ['course']


	@admin.register(Learning)
	class LearningAdmin(admin.ModelAdmin):
    	list_display = ['description', 'course']
    	list_filter = ['course']


	@admin.register(UserCourse)
	class UserCourseAdmin(admin.ModelAdmin):
    	list_display = ['user', 'course', 'date']
    	list_filter = ['user', 'course', 'date']
    	search_fields = ['user__username', 'course__name']

	@admin.register(Video)
	class VideoAdmin(admin.ModelAdmin):
    	list_display = ['title', 'course', 'serial_number']
    	list_filter = ['course']
    	fields = ['title', 'course', 'serial_number','is_preview', 'video_id', 'video_file']  


Here, .models means from this current directory import the category  and course ,usercourse ,video  model, from Models.py file and
for each model to register we need the command --> admin.site.register(model_name)

### server

Now, lets check that our model is being registered properly or not. First lets ensure that our server is running properly. Put the following commmand in terminal:

(django_project)$`python manage.py runserver`

* now open this link in your browser http://127.0.0.1:8000/

You will see a rocket there and a message saying, 'The install worked successfully! Congratulations!'

if yes, we didn't make any mistakes. Good !

* Now go to admin page by using this link http://127.0.0.1:8000/admin/


### views

Now lets see our books on our webpage but before that we need to work on views. In this case im gonna use 'Class Based Views' which makes our code as much DRY (Don't Repeat Yourself) as possible and faster to implement. Put the follwing code in your views.py file.


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
    




* what we done here ? 
1. Importing necessary modules and classes:
   - The code begins by importing various modules and classes required for the views.

2. Category-related Views:
   - `CreateCategoryViewSet`: This view set allows creating, retrieving, updating, and deleting Category objects.
   - `CategoryListAPIView`: This read-only view lists all Category objects.
   - `CategoryDetailAPIView`: This read-only view retrieves a specific Category object by its primary key.

3. Course-related Views:
   - `CourseListAPIView`: This read-only view lists all Course objects.
   - `CreateCourseViewSet`: This view set allows creating, retrieving, updating, and deleting Course objects.
   - `CourseDetailAPIView`: This read-only view retrieves a specific Course object by its primary key.

4. UserCourse-related Views:
   - `UserCourseListAPIView`: This read-only view lists all UserCourse objects.
   - `CreateUserCourseViewSet`: This view set allows creating, retrieving, updating, and deleting UserCourse objects.
   - `UserCourseDetailAPIView`: This read-only view retrieves a specific UserCourse object by its primary key.

5. Video-related Views:
   - `VideoListAPIView`: This read-only view lists all Video objects.
   - `CreateVideoViewSet`: This view set allows creating, retrieving, updating, and deleting Video objects.
   - `VideoDetailAPIView`: This read-only view retrieves a specific Video object by its primary key.

The code follows a modular approach, with each view class handling specific operations related to Categories, Courses, UserCourses, and Videos. It utilizes Django REST Framework's generic views and viewsets for common CRUD operations. Additionally, serializers are used for data serialization and deserialization.




### urls

Now to make our class based views work we need url routing. By default we have a single urls.py file in our fciplatform directory and not in course app. So lets create a urls.py file in our app (why so ? so that django can easily find which url is working for which app, therfore instead of putting all urls in a single file its better to create seperate urls.py file for each app). Inside your course app create a new urls.py file. (you can do it by using your IDE or by following below code)

for linux users

$touch course/urls.py


Before putting some code in this file go to fciplatform folder and open urls.py file. Update this file in the follwing manner

	from django.contrib import admin
	from django.urls import path, include # changes

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', include('course.urls')),  # changes
	]

In short, here im telling django that im using a seperate urls.py file for my course app. Now go back to our app level url.py file (or open the urls.py file of our course app). Put the following code there

	from django.urls import path
	from rest_framework import routers
	from .views import (
    	CreateCategoryViewSet,
    	CategoryListAPIView,
    	CourseListAPIView,
    	CreateCourseViewSet,
    	UserCourseListAPIView,
    	CreateUserCourseViewSet,
    	VideoListAPIView,
    	CreateVideoViewSet,
	)
	from . import views

	router = routers.DefaultRouter()
	router.register(r'categories', CreateCategoryViewSet)
	router.register(r'courses', CreateCourseViewSet)
	router.register(r'courses', CreateUserCourseViewSet)
	router.register(r'videos', CreateVideoViewSet)

	urlpatterns = [
    	path('category/', CategoryListAPIView.as_view(), name='category-list'),
    	path('course/', CourseListAPIView.as_view(), name='course-list'),
    	path('user-course/', UserCourseListAPIView.as_view(), name='user-course-list'),
    	path('video/', VideoListAPIView.as_view(), name='video-list'),

	]+router.urls




* what we done here ? 


Importing necessary modules and classes:

The code imports the path function from django.urls for defining URL patterns.
The routers module from rest_framework is imported for creating default routers.
Various views are imported from the .views module.
Creating a router and registering view sets:

A DefaultRouter object is created.
View sets (CreateCategoryViewSet, CreateCourseViewSet, CreateUserCourseViewSet, and CreateVideoViewSet) are registered with the router for automatic URL routing.
Defining URL patterns:

The urlpatterns list is defined to handle different URLs and associate them with respective views.
path function is used to define URL patterns and map them to corresponding view classes.
CategoryListAPIView is mapped to the URL path 'category/' using the as_view() method.
CourseListAPIView is mapped to the URL path 'course/' using the as_view() method.
UserCourseListAPIView is mapped to the URL path 'user-course/' using the as_view() method.
VideoListAPIView is mapped to the URL path 'video/' using the as_view() method.
The router.urls are appended to the urlpatterns list to include the automatically generated URL patterns for the registered view sets.
Additional commented paths:

Several commented paths are present in the code, which can be uncommented and used to map the corresponding detail views (<int:pk>/) to their respective URLs.



Every time we create a new application, we follow the same steps and add the application within the project settings and upload it to our server.









 

 








































