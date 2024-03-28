from django.db import models
from datetime import datetime,date,time
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
days= (
    ('sat & sun','SAT & SUN'),
    ('mon to fri', 'MON TO FRI'),
)
class nays(models.Model):
    id=models.AutoField(primary_key=True)
    nays=models.CharField(max_length=15, choices=days,default='sat & sun')
    def __str__(self):
        return self.nays

class courseModel(models.Model):
    id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=50,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(default=None)
    day=models.ForeignKey(nays,on_delete=models.CASCADE)
    date=models.DateField(default=datetime.now)
    strtime=models.TimeField(default=datetime.now)
    endtime=models.TimeField(default=datetime.now)
    def __str__(self):
        return self.subject



class userProfileModel(models.Model):
    id=models.AutoField(primary_key=True)
    phone=PhoneNumberField()
    course=models.ForeignKey(courseModel,on_delete=models.CASCADE)
    image=models.ImageField(default=None)
    auth=models.OneToOneField(User,on_delete=models.CASCADE ,default=None)
    userStatus=models.IntegerField(default=None)

    
class joinModel(models.Model):
    id=models.AutoField(primary_key=True)
    auth=models.ForeignKey(User,on_delete=models.CASCADE)
    join_date=models.DateTimeField(default=datetime.now)
   

class record(models.Model):
    id=models.AutoField(primary_key=True)
    cuser=models.ForeignKey(joinModel,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    date=models.DateTimeField(default=datetime.now)
    
    
class notiModel(models.Model):
    id=models.AutoField(primary_key=True)
    header=models.CharField(max_length=20)
    content=models.TextField(default=None)
    file=models.FileField(default=None)
    author=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.header

class reportModel(models.Model):
    id=models.AutoField(primary_key=True)
    about=models.TextField(default=None)


    def __str__(self):
        return self.id