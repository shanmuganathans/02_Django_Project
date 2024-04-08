from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def sign_in(request):
    if request.method =="GET":
        form = LoginForm()
        return render(request,"users/login.html", context={"form":form})
    elif request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("posts")
        messages.error(request, "Your entered Invalid username or passoword")
        return render(request, "users/login.html", {'form':form})
    
def sign_out(request):
    logout(request)
    messages.success(request, "You're logged out.!")
    return redirect("login")

def sign_up(request):
    if request.method =="GET":
        form = RegisterForm()
        return render(request,"users/register.html", context={"form":form})
    elif request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You're signed up successfully")
            return redirect("login")
        else:
            return render(request, "users/register.html",{"form":form})
        