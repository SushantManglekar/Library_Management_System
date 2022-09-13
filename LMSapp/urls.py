from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student, name='student'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_signup', views.admin_signup, name='admin_signup'),
    path('req', views.req, name='req'),  
    path('show',views.show, name='show'),  
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'), 
    
    
 
]