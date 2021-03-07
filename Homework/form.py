from django import forms
from django.forms import ModelForm
from .models import HomeWork,Answer
class creat_homework (ModelForm):
    class Meta :
        model= HomeWork
        fields= '__all__'
# class creat_answer (ModelForm):
#     class Meta :
#         model= Answer
#         fields= '__all__'

class creat_answer (ModelForm):
    class Meta :
        model= Answer
        fields= ['Title_homework', 'student_number','File']