from django.shortcuts import render,redirect
from django.contrib import messages
from library.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def s_logout(request):
    logout(request)
    return redirect('/student/login/')

def s_login(request):
    if request.method == "GET":
        return render(request,'s_login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(Q(email=username) | Q(username=username))
        except Exception:
            return redirect('/student/login/')
        
        if user.check_password(password):
            login(request,user)

            subject='welcome to my school'
            message= f'hi  {user.username}, thanks for login'
            email_from= settings.EMAIL_HOST_USER
            recipient_list=[user.email,]

            send_mail(subject,message,email_from,recipient_list)
            return redirect('/student/dashbook/')
        else:
            return redirect('/student/login/')

def s_register(request):
    if request.method == "GET":
        return render (request, 's_register.html')
    if request.method == "POST":
        userData=User.objects.create(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=make_password(request.POST.get('password')),

        )
    return redirect('/student/login/')


def home(request):
    return render(request,'home.html')

def s_dashbook(request):
    return render(request,'s_dashbook.html')

def s_vprofile(request):
    profile=userProfileModel.objects.get(auth_id=request.user.id)
    return render(request, 's_viewprofile.html',{'profile':profile})

def s_profile(request):
    if request.method=="GET":
        userData=User.objects.get(id=request.user.id)
        try:
            profile = userProfileModel.objects.get(auth_id=request.user.id)
        except Exception:
            course=courseModel.objects.all()
            return render (request, 's_profile.html', { 'userData':userData,'course':course} )
        return render(request, 's_viewprofile.html',{'profile':profile})
    if request.method == "POST":
        userProfileModel.objects.create(
            phone=request.POST.get('phone'),
            image=request.FILES.get('image'),
            course_id = request.POST.get('course'),
            auth_id=request.user.id,
            userStatus= 1,
        )
        return redirect('/student/vprofile/')
    

    
def s_course(request):
    course=courseModel.objects.all()
    if request.method == "GET":
        return render(request, 's_course.html',{'course':course})
    if request.method == "POST":
        joinModel.objects.create(
            auth_id=request.user.id
        )
        return redirect('/student/dashbook/')
        

def s_friend(request):
    friend=userProfileModel.objects.filter(userStatus=1)
    return render(request, 's_friend.html',{'friend':friend})

def s_notification(request):
    noti=notiModel.objects.all()
    return render(request, 's_notification.html',{'noti':noti})

def s_certificate(request):
    return render(request, 's_certificate.html')

def s_record(request):
    record.objects.create(
        cuser_id=request.user.id,
        active = True
    )
    return redirect('/student/dashbook/')