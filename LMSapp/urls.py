from django.contrib import admin
from django.urls import path
from . import views
from .views import Library_Manager, Book_Details

urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_signup', views.admin_signup, name='admin_signup'),
    path('booklist', views.booklist, name='booklist'),
    path('api/library_manager', Library_Manager.as_view()),
    path('api/library_manager/<int:pk>', Book_Details.as_view())
]