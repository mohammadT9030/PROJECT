"""djangoProject16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from Video.views import student_videos,teacher_videos,upload_video,Home,teacher,student
from Homework.views import student_homework,teacher_homework,upload_homework,upload_answer,view_answer
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name='Home'),
    path('student/',student, name='student'),
    path('student/videos/', student_videos, name='student_videos'),
    path('teacher/', teacher, name='teacher'),
    path('teacher/videos/', teacher_videos, name='teacher_videos'),
    path('teacher/videos/upload/',upload_video,name='upload_video'),
    path('student/homework/', student_homework, name='student_homework'),
    path('student/homework/upload/',upload_answer,name='upload_answer'),
    path('teacher/homework/',teacher_homework, name='teacher_homework'),
    path('teacher/homework/upload/',upload_homework,name='upload_homework'),
    path('teacher/homework/<str:hw_title>/',view_answer,name='view_answer'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)