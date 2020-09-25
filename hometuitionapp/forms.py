from django import forms
from django.contrib.auth.models import User
from .models import *


class StudentLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter your username..",
        "class": "form-control",

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password ....",
        "class": "form-control",

    }))


class StudentSignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        uname = self.cleaned_data["username"]
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "User with this user name already exists")
        return uname

    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        c_pword = self.cleaned_data["confirm_password"]
        if password != c_pword:
            raise forms.ValidationError("Password did not match")
        return c_pword


class TeacherLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter your username..",
        "class": "form-control",

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password ....",
        "class": "form-control",

    }))


class TeacherSignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        uname = self.cleaned_data["username"]
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "User with this user name already exists")
        return uname

    def clean_confirm_password(self):
        password = self.cleaned_data["password"]
        c_pword = self.cleaned_data["confirm_password"]
        if password != c_pword:
            raise forms.ValidationError("Password did not match")
        return c_pword

# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput())
#     email = forms.CharField(widget=forms.EmailInput())
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())

#     def clean_username(self):
#         uname = self.cleaned_data["username"]
#         if User.objects.filter(username=uname).exists():
#             raise forms.ValidationError(
#                 "User with this username already exists")
#         return uname

#     def clean_confirm_password(self):
#         password = self.cleaned_data["password"]
#         c_pword = self.cleaned_data["confirm_password"]
#         if password != c_pword:
#             raise forms.ValidationError("Password did not match")
#         return c_pword

#     def clean_email(self):
#         email = self.cleaned_data["email"]
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError(
#                 "Email with this email address already exists")
#             return email


class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = Teacher
        # fields = ["username", "email", "password", "confirm_password",
        #           "name", "gender", "photo", "phone_no", "address",
        #           "education", "experience", "cv", "citizenship", "subject"]
        fields = "__all__"


class HomeTuitionSystemForm(forms.ModelForm):
    class Meta:
        model = HomeTuitionSystem
        fields = "__all__"


class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter your username...",
        "class": "form-control"

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password...",
        "class": "form-control",

    }))
