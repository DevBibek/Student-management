from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_age = models.IntegerField()
    student_roll = models.IntegerField()
    student_addre = models.CharField(max_length=100)