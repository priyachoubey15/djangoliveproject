from django.db import models

# Create your models here.

class student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.BigIntegerField()
