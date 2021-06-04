from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course_Django(request):
    return HttpResponse('WEL-COME IN DJANGO COURSE')

def course_Python(request):
    return HttpResponse('WEL-COME IN PYTHON COURSE')
