from django.db import models

# Create your models here.
class TeacherVideo (models.Model):
    Title=models.CharField(max_length=50)
    VideoFile=models.FileField(upload_to='VideoFolder')

    def __str__(self):
        return self.Title