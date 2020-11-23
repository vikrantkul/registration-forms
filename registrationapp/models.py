from django.db import models
from django.contrib.auth import views
import datetime
from datetime import date
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    num=models.IntegerField()
    name=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    Age=models.IntegerField()
    Address=models.CharField(max_length=50)
    note = models.CharField(max_length=25,null=True)
    birthdate=models.DateField(default=timezone.now)
    gender=models.CharField(max_length=25,null=True)
    def __str__(self):
        return self.name

GENDER_CHOICES = (
    ('Male','MALE'),
    ('Female', 'FEMALE'),
    ('Other','OTHER'),
)

CLASS_CHOICES=(
    ('Physics','PHYSICS'),
    ('Chemistry','CHEMISTRY'),
    ('Maths','MATHS'),
)



class Personal(models.Model):
    name=models.CharField(max_length=25)
    birthday=models.CharField(max_length=25)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES, default=None)
    subject=models.CharField(max_length=25, choices=CLASS_CHOICES, default=None)
    res_code=models.CharField(max_length=25)
    def __str__(self):
        return self.name