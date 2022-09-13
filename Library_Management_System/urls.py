
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls), 
    path('',include('LMSapp.urls')), # Added URL of app's root directory 
]
