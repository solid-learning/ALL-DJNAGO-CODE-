from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course(request):
  
    return render(request,'cor/course.html' ,{'key':'WEL-COME IN WEB DEVLOPMENT COURSE DDDDJANGO'})

def Fees(request):
    stor={'djfee':'499','pyfee':'399','javafee':'450'}
    return render(request,'cor/fee.html',stor)

def contact(request):
    django="fill the 1st form for enroll in Django"
    python="fill the 2ed form for enroll in PYTHON"
    java="fill the 3rd form for enroll in JAVA"
    web="fill the 4th form for enroll in front end WEB-DEVLOPMENT"
    con={'dj':django ,'py':python ,'ja':java,'webd':web}
    return render(request,'cor/contact.html', context=con)