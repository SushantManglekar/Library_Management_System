import email
from email.mime import message
import json
import pkgutil
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import request
from rest_framework import generics
from .models import Book
from .forms import ManageForm
from .serializers import BookSerializer
from LMSapp import serializers

# View for the root URL
def index(request):
    return render(request, 'index.html')



# View for the dmin_login/ URL
def admin_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('psw')
        # uthentication of user
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('show') # redirecting to Booklist page
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
        elif User.objects.filter(username= username).exists():
            messages.info(request, "username already exists!") # validating duplicate entry
            return redirect('admin_signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password) # Creating user in database
            user.save()
            print("User Created!")
            return redirect('admin_login')
    else:
        return render(request, "admin_signup.html")




def req(request):  
    if request.method == "POST":  
        form = ManageForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ManageForm()  
    return render(request,'add.html',{'form':form})  



def show(request):  
    books = Book.objects.all()  
    return render(request,"show.html",{'books':books})  


def edit(request, id):  
    book = Book.objects.get(id=id)  
    return render(request,'edit.html', {'book':book})



def update(request, id):  
    book = Book.objects.get(id=id)  
    form = ManageForm(request.POST, instance = book)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'book': book})  

def destroy(request, id):  
    book = Book.objects.get(id=id)  
    book.delete()  
    return redirect("/show")  


def student(request):
    books = Book.objects.all()
    return render(request,'student.html',{'books':books})