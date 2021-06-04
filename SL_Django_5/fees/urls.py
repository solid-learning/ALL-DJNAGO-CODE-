from django.urls import path
from . import views

urlpatterns = [
    path('feedj/',views.Fee_Django),

    path('feepy/',views.Fee_Python),

    path('feepy/',views.Fee_java),

    path('feepy/',views.Fee_cpp)
]