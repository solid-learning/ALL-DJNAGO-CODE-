from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Fees_Django(request):
    return render(request,'feesone.html',)

def Fees_Python(request):
    return render(request,'feestwo.html')
