from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'cor/home.html',{'home':'active'})

def contact(request):
    return render(request,'cor/contact.html' ,{'contactus':'active'})