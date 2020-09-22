from django import forms
from django.contrib.auth.models import User
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter your username..",
        "class": "form-control",

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password ....",
        "class": "form-control",

    }))


class SignupForm(forms.Form):
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


class HomeTuitionSystemForm(forms.ModelForm):
    class Meta:
        model = HomeTuitionSystem
        fields = "__all__"
