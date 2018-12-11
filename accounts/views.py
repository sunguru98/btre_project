from django.shortcuts import render, redirect 
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == "POST":
        first_name = request.POST['fisrt_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please try again")
                return redirect('accounts:signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists. Please try again")
                    return redirect('accounts:signup')
                else:
                    new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                    new_user.save()
                    messages.success(request, "User registered successfully. Please Login")
        else:
            messages.error(request, "Passwords do not match. Please try again")
            return redirect('accounts:signup')
    else:       
        return render(request, "accounts/signup.html")

def dashboard(request):
    return render(request, "accounts/dashboard.html")

def login(request):
    return render(request, "accounts/login.html")

def logout(request):
    return redirect("index")