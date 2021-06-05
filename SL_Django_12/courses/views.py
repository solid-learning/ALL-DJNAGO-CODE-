from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course_Django(request):
    return render(request,'courses/course.html' ,{'key':'THIS IS THE BEST WEB DEVLOPMENT COURSE  DDDJANGO'})

