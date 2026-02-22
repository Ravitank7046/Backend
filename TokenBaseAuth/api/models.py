from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  aadharNumber = models.IntegerField()
  schoolName = models.CharField(max_length=100)
  
