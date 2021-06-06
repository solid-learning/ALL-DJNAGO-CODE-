from django.urls import path
from . import views

urlpatterns = [
    path('course/',views.course),
    path('fee/',views.Fees),
    path('contact/',views.contact),
    ]