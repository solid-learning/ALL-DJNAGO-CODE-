from django.shortcuts import render
from enroll.models import Student
# Create your views here.

def home(request):
    stu=Student.objects.all()
    return render(request,'enroll/home.html',{'stud':stu})