from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    #path to root directory of app
    path('', views.index, name='index'),
    #path to only view books in library
    path('student', views.student, name='student'),
    #path to admin login page
    path('admin_login', views.admin_login, name='admin_login'),
    #path to admin signup page
    path('admin_signup', views.admin_signup, name='admin_signup'),
    # path to add book 
    path('req', views.req, name='req'),  
    # path to admin view access
    path('show',views.show, name='show'),  
    #path to edit existing book
    path('edit/<int:id>', views.edit, name='edit'),  
    #path to update book
    path('update/<int:id>', views.update, name='update'),  
    # path to delete a book
    path('delete/<int:id>', views.destroy, name='destroy'), 
    
    
 
]