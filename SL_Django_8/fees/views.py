from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Fees_Django(request):
    return render(request,'fees/feesone.html',)

def Fees_Python(request):
    return render(request,'fees/feestwo.html')
