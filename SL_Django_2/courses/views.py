from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course_Django(request):
    return HttpResponse("wel-come in Django")

def course_Python(request):
    return HttpResponse("wel-come in python")