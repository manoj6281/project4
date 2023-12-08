from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def waste(request):
    return render(request,'waste.html')



def manoj(request):
    return HttpResponse('<h1><marquee>Hii hello manoj kumar</marquee></h1')