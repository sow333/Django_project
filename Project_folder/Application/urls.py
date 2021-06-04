from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('App.urls')),
    path('App/', include('App.urls')),
    path('admin/', admin.site.urls),
    path('multiple_views/', include('multiple_views.urls')),
]
