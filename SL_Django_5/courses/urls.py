from django.urls import path
from courses import views

urlpatterns = [
    path('coursedj/',views.course_Django),

    path('coursepy/',views.course_Python),

    path('coursejava/',views.course_java),

    path('coursecpp/',views.course_cpp)
    
]