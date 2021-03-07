from django.shortcuts import render
from .form import creat_homework,creat_answer
from django.http import HttpResponse
from .models import HomeWork,Answer
from django.contrib.auth import login
# Create your views here.

def student_homework (request):
    homework= HomeWork.objects.all()
    answer = Answer.objects.all()
    context={
        'hw': homework,
        'answer': answer,
    }
    return render(request,'student_homework.html',context)

def teacher_homework (request):
    homework= HomeWork.objects.all()
    context={
        'hw': homework
    }
    return render(request,'teacher_homework.html',context)

def view_answer (request,hw_title):
    answers= Answer.objects.filter(Title_homework=hw_title)
    context={
        'answers':answers
    }
    return render(request,'view_answers.html',context)

def upload_homework (request):
    form = creat_homework()
    if request.method=='POST':
        form= creat_homework(request.POST,request.FILES)
        if form .is_valid():
            form.save()
            return HttpResponse('Uploaded')
    context={
        'form':form,
    }
    return render(request,'upload_homework.html',context)

def upload_answer (request):
    form = creat_answer()
    if request.method=='POST':
        form= creat_answer(request.POST,request.FILES)
        if form .is_valid():
            form.save()
            return HttpResponse('Uploaded')
    context={
        'form':form,
    }
    return render(request,'upload_answer.html',context)