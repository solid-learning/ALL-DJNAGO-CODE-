from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def URL_IN_APPLICATION(request):
    return HttpResponse("<h1> WEL-COME IN DJANGO'S NEW VERSION</h1>")