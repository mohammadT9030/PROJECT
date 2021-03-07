from django import forms
from django.forms import ModelForm
from .models import TeacherVideo
class creat_video (ModelForm):
    class Meta :
        model= TeacherVideo
        fields= '__all__'