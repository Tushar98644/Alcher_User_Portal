from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
   
    path('webops2', views.secondpage,name='secondpage'),
]
