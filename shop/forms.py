from django import forms
from django.contrib.auth.models import User
import re


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form_input", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form_input", "placeholder": "Password"}))


    def clean_username(self):
        value = self.cleaned_data['username']

        if re.fullmatch(r"[A-Za-z0-9]{8}", value) is None:
            raise forms.ValidationError("username 8 xonali katta kichik harflar va raqamlardan bo'lishi kerak")
        
        return value
    
    def clean_password(self):
        value = self.cleaned_data['password']

        if re.fullmatch(r"[A-Za-z0-9]{8}", value) is None:
            raise forms.ValidationError("password 8 xonali katta kichik harflar va raqamlardan bo'lishi kerak")
        
        return value
    
    
class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "from_input", "placeholder": "Firstname"}), required = True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "from_input", "placeholder": "Lastname"}), required = True)
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "from_input", "placeholder": "Username"}), required = True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "from_input", "placeholder": "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "from_input", "placeholder": "Password"}), required = True)
    reset_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "from_input", "placeholder": "Reset password"}), required = True)


    def clean_first_name(self):
        value = self.cleaned_data['first_name']

        if not re.fullmatch(r"[A-Za-z]+", value):
            raise forms.ValidationError("First name faqat harflardan iborat bo'lishi kerak")
            
    
    def clean_last_name(self):
        value = self.cleaned_data['last_name']

        if not re.fullmatch(r"[A-Za-z]+", value):
            raise forms.ValidationError("Last name faqat harflardan iborat bo'lishi kerak")
        
        return value

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if username is None:
            raise forms.ValidationError("username kiritilishi shart")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bunday user bazada mavjud")

        return username
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if email is None:
            raise forms.ValidationError("email kiritilishi shart")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Bunday email bazada mavjud")
        
        return email
    
    def clean_reset_password(self):
        password = self.cleaned_data.get('password')
        reset_password = self.cleaned_data.get('reset_password')


        if password != reset_password:
            raise forms.ValidationError("Parollar bir xil bo'lishi kerak")
        
        return password
    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        if not re.fullmatch(r"[A-Za-z0-9]{8}", password):
            raise forms.ValidationError("Password 8 xonali katta-kichik harflar va raqamlardan iborat bo'lishi kerak")
        
        return password

