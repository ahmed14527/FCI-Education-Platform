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
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        return obj.thumbnail.url

    class Meta:
        model = Course
        fields = ('category', 'name', 'description', 'discount', 'active', 'thumbnail', 'date', 'resource', 'length')


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
    video_file = serializers.SerializerMethodField()

    def get_video_file(self, obj):
        return obj.video_file.url

    class Meta:
        model = Video
        fields = ('title', 'serial_number', 'course', 'video_id', 'video_file', 'is_preview')
        
        
class VideoDetailSerializer(serializers.ModelSerializer):
    model = Video
    fields = '__all__'


        