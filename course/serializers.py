from rest_framework import serializers
from .models import Course,Category, UserCourse, Video
from rest_framework import serializers
from .models import Course, Category, UserCourse, Video
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class CategoryDetailSerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'
            
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    model = Course
    fields = '__all__'
    
    

        
class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'
        
        
class UserCourseDetailSerializer(serializers.ModelSerializer):
    model = UserCourse
    fields = '__all__'
 
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
        
class VideoDetailSerializer(serializers.ModelSerializer):
    model = Video
    fields = '__all__'


        