from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse
# Create your views here.
def loginview_teach(request):
    if request.method == "POST":
        username = request.POST['username']
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            f=open('usfile.txt','w')
            f.write(username)
            f.close()
            return redirect('/teacher')
    form=AuthenticationForm()
    return render(request, 'login.html', {'form': form })

def loginview_stu(request):
    if request.method == "POST":
        username = request.POST['username']
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            f=open('usfile.txt','w')
            f.write(username)
            f.close()
            return redirect('/student')
    form=AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# def user(request):
#     form= AuthenticationForm(data=request.POST)
#     user=form.get_user()
#     return (render,'student_homework.html',{'us':user})