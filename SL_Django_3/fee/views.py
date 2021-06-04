from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Fee_Django(request):
    return HttpResponse('DJANGO COURSE FEE == 499 RU. ONLY')

def Fee_Python(request):
    return HttpResponse('PYTHON COURSE FEE == 349 RU. ONLY')
