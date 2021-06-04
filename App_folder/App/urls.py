from django.urls import path
from . import views

urlpatterns=(
    path('App/', views.App, name="App"),
    path('', views.App_home, name="App_home"),
)
