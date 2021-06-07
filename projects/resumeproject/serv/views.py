from django.shortcuts import render

# Create your views here.
def servises(request):
    return render(request,'serv/myserv.html' , {'myservises':'active'})