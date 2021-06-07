from django.urls import path
from . import views
urlpatterns = [
 path('servises/', views.servises , name='myservises')
  
]