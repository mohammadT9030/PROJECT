from django.shortcuts import render
from .form import creat_video
from django.http import HttpResponse
from .models import TeacherVideo
# Create your views here.

def Home (request):
    return render(request,'home.html')

def student (request):
    return render(request,'student.html')

def teacher (request):
    return render(request,'teacher.html')

# def student_videos (request):
#     return render(request,'student_videos.html')

def teacher_videos (request):
    videos= TeacherVideo.objects.all()
    context={
        'video': videos
    }
    return render(request,'teacher_videos.html',context)

def student_videos (request):
    videos= TeacherVideo.objects.all()
    context={
        'video': videos
    }
    return render(request,'student_videos.html',context)

def upload_video (request):
    form = creat_video()
    if request.method=='POST':
        form= creat_video(request.POST,request.FILES)
        if form .is_valid():
            form.save()
            return HttpResponse('Uploaded')
    context={
        'form':form,
    }
    return render(request,'upload_video.html',context)