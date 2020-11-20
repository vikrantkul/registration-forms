from django.db import models

# Create your models here.
class Student(models.Model):
    num=models.IntegerField()
    name=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    Age=models.IntegerField()
    Address=models.CharField(max_length=50)


    def __str__(self):
        return self.name
