from django.conf.urls import url
from django.urls import path
from .views import person
from .views import req

urlpatterns = [
    path('about/', req.about, name="about"),
    path('showContact/', req.showContact, name="showContact"),
    path('hello/', req.hello, name="hello"),
    path('simple_intrest/', person.simple_intrest, name="simple_intrest"),
    path('compound_intrest/', person.compound_intrest, name="compound_intrest"),
    ]
