from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'cor/home.html')

def courses(request):
    return render(request,'cor/courses.html')