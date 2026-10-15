from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Glassary! <br/> <a href='/glassary/about/'>About</a>")

def about(request):
    return HttpResponse("This is the Glassary about page! <br/> <a href='/glassary/'>Index</a>")