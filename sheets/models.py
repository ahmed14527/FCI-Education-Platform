from django.db import models


class Sheet(models.Model):
    file = models.FileField(upload_to='files/sheets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name