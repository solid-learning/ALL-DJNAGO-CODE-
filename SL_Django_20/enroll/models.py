from django.db import models
# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=40)
    stuemail=models.EmailField(max_length=40)
    stucollage=models.CharField(max_length=40)
    stustate=models.CharField(max_length=40)
  

    
    
