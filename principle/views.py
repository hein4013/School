from django.shortcuts import render,redirect
from django.contrib import messages
from library.models import *
from principle.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password




# Create your views here.
def t_logout(request):
    logout(request)
    return redirect('/teacher/login/')

def t_login(request):
    if request.method == "GET":
        return render(request,'t_login.html')
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/teacher/dashbook/')
        else:
            return redirect('/teacher/login/')
        
def t_register(request):
    if request.method == "GET":
        return render (request, 't_register.html')
    if request.method == "POST":
        userData=User.objects.create(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=make_password(request.POST.get('password')),
        )
    return redirect('/teacher/login/')

def t_dashbook(request):
    return render(request,'t_dashbook.html')

def t_vprofile(request):
    profile=teacherProfileModel.objects.get(auth_id=request.user.id)
    return render(request, 't_viewprofile.html',{'profile':profile})


def t_profile(request):
    if request.method=="GET":
        userData=User.objects.get(id=request.user.id)
        try:
            profile = teacherProfileModel.objects.get(auth_id=request.user.id)
        except Exception:
            return render (request, 't_profile.html', { 'userData':userData} )
        return render(request, 't_viewprofile.html',{'profile':profile})
    if request.method == "POST":
        teacherProfileModel.objects.create(
            phone=request.POST.get('phone'),
            image=request.FILES.get('image'),
            auth_id=request.user.id,
            userStatus= 2,
        )
        return redirect('/teacher/vprofile/')

def t_course(request):
    nay=nays.objects.all()
    if request.method =="GET":
        return render(request,'t_course.html',{'nay':nay})
    if request.method == "POST":
        courseModel.objects.create(
        subject=request.POST.get('subject'),
        content=request.POST.get('content'),
        day_id=request.POST.get('nays'),
        author_id=request.user.id,
        date=request.POST.get('date'),
        strtime =request.POST.get('strtime'),
        endtime =request.POST.get('endtime'),
        )
    return redirect('/teacher/course/')

def t_timetable(request):
    course=courseModel.objects.filter(author_id=request.user.id)
    return render(request, 't_timetable.html',{'course':course})

def t_friend(request):
    friend=teacherProfileModel.objects.filter(userStatus=2)
    return render(request, 't_friend.html',{'friend':friend})

def t_notification(request):
    if request.method == "GET":
        return render(request,'t_notification.html')
    if request.method == "POST":
        notiModel.objects.create(
            header=request.POST.get('header'),
            content=request.POST.get('content'),
            file=request.FILES.get('file'),
            author_id=request.user.id
        )
    return redirect('/teacher/dashbook/')

def t_onlynoti(request):
    uu=User.objects.all()
    if request.method == "GET":
        return render(request,'t_onlynoti.html',{'uu':uu})
    if request.method == "POST":
        notiModel.objects.create(
            header=request.POST.get('header'),
            content=request.POST.get('content'),
            file=request.FILES.get('file'),
            author_id=request.user.id
        )
    return redirect('/teacher/dashbook/')

def t_studentList(request):
    list=joinModel.objects.all()
    return render(request, 't_studentList.html',{'list':list})

def t_check(request):
    check=record.objects.filter(active=True)
    return render(request, 't_report.html',{'check':check})