from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course_Django(request):
    return render(request,'courses/courseone.html')

def course_Python(request):
    return render(request,'courses/coursetwo.html')

def course(request):
    return render(request,'course.html')