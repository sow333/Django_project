from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def App(request):
    return HttpResponse("Welcome to Django Web page")

def App_home(request):
    return HttpResponse("My First Django Application")
