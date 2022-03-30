from statistics import mode
from django.db import models

class AppliedUser(models.Model):
    name = models.CharField(max_length=20, unique=False)
    designation = models.CharField(max_length=20)
    org = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    qualification = models.CharField(max_length=40)
    expertise = models.CharField(max_length=100)
    
