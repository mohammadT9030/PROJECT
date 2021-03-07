from django.db import models

# Create your models here.
class HomeWork(models.Model):
    Title=models.CharField(max_length=50)
    HWFile= models.FileField(upload_to='HomeWorkFolder')

    def __str__(self):
        return self.Title


class Answer(models.Model):
    Title_homework= models.CharField(max_length=50)
    student_number= models.CharField(max_length=50)
    last_post_time = models.DateTimeField(auto_now=True)
    File = models.FileField(upload_to='AnswerFolder')
    score= models.IntegerField(default=-1,)