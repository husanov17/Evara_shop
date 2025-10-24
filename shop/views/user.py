from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.forms import LoginForm, RegisterForm
from django.views.generic import View
from shop.utils import Cart
from django.contrib import messages


class ProfileUserView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        context = {
            "cart": cart,
            "user": request.user
        }
        return render(request, "shop/profile.html", context)

    def post(self, request):
        user = request.user
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if first_name and last_name:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, "Profil ma'lumotlari yangilandi")
        else:
            messages.warning(request, "First name va Last name kiritilsin")
        
        return redirect("profile")



class ChangePasswordView(View):
    def post(self, reuqest):
        old_password = reuqest.POST.get("old_password")
        new_password = reuqest.POST.get("new_password")
        repeat_new_password = reuqest.POST.get("repeat_new_password")

        user = reuqest.user
        if user.check_password(old_password) and new_password==repeat_new_password:
            user.set_password(new_password)
            user.save()
        
        return redirect("profile")


class LoginUserView(View):
    def get(self, request):
        form = LoginForm()
        data = {
            "path": "Login",
            "form": form
        }

        return render(request, "shop/login.html", context=data)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Siz muvaffaqqiyatli login qildingiz")
                return redirect("dashboard")
        messages.error(request, "Login yoki parol xato")
            
        data = {
                "path": "Login",
                "form": form
            }
        return render(request, "shop/login.html", context=data)
            

def logout_user(request):
    logout(request) 
    messages.success(request, "Siz tizimdan chiqdingiz.")
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
            "path": 'Register',
            "form": form
        }
        return render(request, "shop/register.html", context=data)

    form = RegisterForm()
    data = {
        "path": 'Register',
        "form": form
    }
    return render(request, "shop/register.html", context=data)