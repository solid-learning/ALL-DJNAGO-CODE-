from django.urls import path
from . import views

urlpatterns = [
    path('feedj/',views.Fee_Django),

    path('feepy/',views.Fee_Python),

    path('feejava/',views.Fee_java),

    path('feecpp/',views.Fee_cpp)
]