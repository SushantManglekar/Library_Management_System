import email
from email.mime import message
import pkgutil
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import request
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# View for the root URL
def index(request):
    return render(request, 'index.html')


# View for the student/ URL
def student(request):
    return render(request, "student.html")
# View for the dmin_login/ URL
def admin_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('psw')
        # uthentication of user
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('booklist') # redirecting to Booklist page
        else:
            # Validating credentials
            messages.info(request,'Invalid Credentials') 
            return redirect('admin_login')
    else:
        return render(request, "admin_login.html")

# view for the sign up form
def admin_signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        if User.objects.filter(email= email).exists():
            messages.info(request, "Email already exists!") # validating duplicate entry
            return redirect('admin_signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password) # Creating user in database
            user.save()
            print("User Created!")
            return redirect('admin_login')
    else:
        return render(request, "admin_signup.html")



def booklist(request):
    return render(request, 'booklist.html')



class Library_Manager(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Book_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer