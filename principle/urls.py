from django.urls import path,include
from principle.views import *

urlpatterns = [
    path('login/',t_login),
    path('logout/',t_logout),
    path('register/',t_register),
    path('dashbook/',t_dashbook),
    path('profile/',t_profile),
    path('vprofile/',t_vprofile),
    path('course/',t_course),
    path('timetable/',t_timetable),
    path('friend/',t_friend),
    path('notification/', t_notification),
    path('onlynoti/', t_onlynoti),
    path('report/',t_check),
    path('studentList/', t_studentList),
    path('checkin/',t_check)
]