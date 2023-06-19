
from django.shortcuts import render

def Home(request):
    return render (request,'home.html')


def meetings(request):
    return render (request,'videochat.html')
    