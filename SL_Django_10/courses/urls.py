from django.urls import path
from . import views

urlpatterns = [
    path('coursedj/',views.course_Django),

    path('coursepy/',views.course_Python),

    path('course',views.course),
   
]