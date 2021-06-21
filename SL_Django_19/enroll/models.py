from django.db import models
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    mail=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    collage=models.CharField(max_length=40)
    
        #   DATE BASE CONFIGRATION
# 1. After write this code we are apply (python manage.py makemigrations) command in terminal 
# 2. Than after we are apply (python manage.py migrate command)

  

# FOR SEE YOUR DATABASE TABLE IN DJANGO ADMINSTRATIONS 
# YOU MUST CREATE SUPERUSER FOR YOUR WEBSITE
# For create superuser you can apply (python manage.py createsuperuser) command in terminal
# and input your 1. username  2. email id 3. password 