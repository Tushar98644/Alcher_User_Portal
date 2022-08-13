from django.shortcuts import render
from django.http import HttpResponse
from .models import post

def home(request):

    post1 = post()
    post1.likes='1like'
    

    post2= post()
    post2.likes='2likes'

    post3 = post()
    post3.likes='3likes'


    post4 = post()
    post4.likes='4likes'


    post5 = post()
    post5.likes='5likes'

    posts=[post1,post2,post3,post4,post5]

    return render(request,'project.html',{'posts':posts}) 