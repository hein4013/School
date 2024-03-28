from django.db import models
from datetime import datetime,date,time
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class teacherProfileModel(models.Model):
    id=models.AutoField(primary_key=True)
    phone=PhoneNumberField()
    image=models.ImageField(default=None)
    auth=models.OneToOneField(User,on_delete=models.CASCADE ,default=None)
    userStatus=models.IntegerField(default=None)
