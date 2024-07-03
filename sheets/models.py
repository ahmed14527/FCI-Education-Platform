from django.db import models
from course.models import Course


    
    
class Sheets(models.Model):
    file=models.FileField(upload_to='files/sheets/')
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    