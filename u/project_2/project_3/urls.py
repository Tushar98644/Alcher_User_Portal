from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
   
    path('project-3', views.mainpage,name='mainpage'),
    
]
