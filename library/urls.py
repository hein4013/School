from django.urls import path,include
from library.views import *


urlpatterns = [
    path('login/', s_login),
    path('register/',s_register),
    path('dashbook/',s_dashbook),
    path('profile/',s_profile),
    path('vprofile/',s_vprofile),
    path('course/',s_course),
    path('friend/',s_friend),
    path('record/',s_record),
    path('notification/', s_notification),
    path('certificate/',s_certificate),
    path('logOut/',s_logout)
]