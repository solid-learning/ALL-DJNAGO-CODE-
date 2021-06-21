from django.shortcuts import render
from fees.models import Student
# Create your views here.

def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        mail=request.POST['mail']
        print(name,mail)
        deepak=Student(name=name,mail=mail)
        deepak.save()

    return render(request,'fees/form.html')

  