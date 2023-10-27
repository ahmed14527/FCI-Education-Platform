from rest_framework import serializers
from .models import Course,Tag, Prerequisite,Category, Learning, UserCourse, Video

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


        
        




    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
        
class PrerequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerequisite
        fields = '__all__'

class CreatePrerequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerequisite
        fields = '__all__'
        
        
class LearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learning
        fields = '__all__'
        
        
class CreateLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learning
        fields = '__all__'
        
        
class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'


class CreateUserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = '__all__'
    
        
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        

class CreateVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        