from operator import mod
from django.db import models

# Create your models here.
class Question(models.Model):

    content=models.TextField()
    op1=models.CharField(max_length=25)
    op2=models.CharField(max_length=25)
    op3=models.CharField(max_length=25)
    op4=models.CharField(max_length=25)
    answer=models.CharField(max_length=25)
    tags=models.CharField(max_length=50)
    difficulty=models.IntegerField()
    isVerified=models.BooleanField(default=False)
    createdAt=models.DateTimeField(auto_now_add=True)

