from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def simple_intrest(request):
    principle = 1000
    rate = 3.5
    time = 10
    response=(principle*rate*time)/100
    return HttpResponse(response)

def compound_intrest(request):
    principle=10000
    rate=10.25
    time=5
    amount = principle * (pow((1 + rate / 100), time))
    response = amount - principle
    return HttpResponse(response)
