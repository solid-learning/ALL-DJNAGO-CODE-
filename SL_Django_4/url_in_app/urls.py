from django.urls import path
from url_in_app import views
urlpatterns = [
   path('app_url/', views.URL_IN_APPLICATION)
]