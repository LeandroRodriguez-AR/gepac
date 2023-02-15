from django.contrib import admin
from django.urls import include, path
from gepapp import views

URLPattern[
    path('admin/', admin.site.urls),
    #path('/gepapp/', include('gepapp.urls')),
          
          ]