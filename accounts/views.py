from django.shortcuts import render, redirect 
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from enquiries.models import Enquiry
# Create your views here.

def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
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
                    return redirect("accounts:login")
        else:
            messages.error(request, "Passwords do not match. Please try again")
            return redirect('accounts:signup')
    else:       
        return render(request, "accounts/signup.html")

@login_required
def dashboard(request):
    enquiries = Enquiry.objects.order_by("-enquiry_date").filter(user_id=request.user.id)
    context = {
        'enquiries':enquiries
    }
    return render(request, "accounts/dashboard.html", context)

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                messages.success(request, "Login Successful")
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Oops! Incorrect Username or password. Please try again")
                return redirect("accounts:login")
        else:    
            return render(request, "accounts/login.html")
    
    else:
        return redirect("index")

@login_required
def user_logout(request): 
    if request.method == "POST":   
        logout(request)
        messages.success(request, "You are logged out")
        return redirect("index")