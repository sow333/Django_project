from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    s="<h1>Hello User and Welcome to first View of testapp</h1><p>This is landing page</p>"
    return HttpResponse(s)

def showContact(request):
    s="""<h1>Contact Page</h1>
    <p>Website: educba.com</p>
    <p>Mobile: +919945678910</p>
    <p>Email: something@gmail.com</p>"""
    return HttpResponse(s)

def about(request):
    s="""<h3>State Bank of India (SBI) is an Indian multinational, public sector banking and financial services statutory body headquartered in Mumbai, Maharashtra. SBI is the 43rd largest bank in the world and ranked 221st in the Fortune Global 500 list of the world's biggest corporations of 2020, being the only Indian bank on the list.It is a public sector bank and the largest bank in India with a 23% market share by assets and a 25% share of the total loan and deposits market.
The bank descends from the Bank of Calcutta, founded in 1806 via the Imperial Bank of India, making it the oldest commercial bank in the Indian Subcontinent. The Bank of Madras merged into the other two presidency banks in British India, the Bank of Calcutta and the Bank of Bombay, to form the Imperial Bank of India, which in turn became the State Bank of India in 1955.
The Government of India took control of the Imperial Bank of India in 1955, with Reserve Bank of India (India's central bank) taking a 60% stake, renaming it State Bank of India.</h3>"""
    return HttpResponse(s)
