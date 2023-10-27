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
    thumbnail = models.ImageField(upload_to = "files/thumbnail") 
    date = models.DateTimeField(auto_now_add= True) 
    resource = models.FileField(upload_to = "files/resource")
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
    
    
def upload_path(instance, filename):
    """Generate the upload path for the video file."""
    return f'course_videos/{instance.course.slug}/{filename}'


class Video(models.Model):
    title  = models.CharField(max_length = 100 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length = 100 , null = False)
    is_preview = models.BooleanField(default = False)
    video_file = models.FileField(upload_to=upload_path)

    def __str__(self):
        return self.title
    
    


    