from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from shop.forms import LoginForm, RegisterForm


def accounts(request):
    return render(request, "shop/accounts.html")


def cart_(request):
    return render(request, "shop/cart.html")


def compare(request):
    return render(request, "shop/compare.html")


def login_register(request):
    return render(request, "shop/login-register.html")


def wishilst(request):
    return render(request, "shop/wishlist.html")

@login_required
def profile_user(request):
    data = {
        "path": "Profilm"
    }
    return render(request, "shop/accounts.html", context=data)


def login_user(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password) 
            if user is not None:
                login(request, user)
                return redirect("dashboard")
        
        else:
            data = {
                "path": "Login",
                "form": form,
            }
            return render(request, "shop/login-register.html", context=data)
        
    form = LoginForm()

    data = {
                "path": "Login",
                "form": form,
            }
    
    return render(request, "shop/login-register.html", context=data)

        
def logout_user(request):
    logout(request)
    return redirect("dashboard")


def register_user(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User(first_name=first_name, last_name=last_name, username=username, email=email)
            user.set_password(password)

            user.save()
            return redirect('login_user')
        else:
            data = {
            "path": "Register",
            "form": form
        }
        return render(request, "shop/register.html", context=data) 


    form = RegisterForm()
    data = {
        "path": "Register",
        "form": form,
    }
    return render(request, "shop/register.html", context=data)
