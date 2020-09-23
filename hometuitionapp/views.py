from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *


class HomeView(TemplateView):
    template_name = "clienttemplates/home.html"


class AboutusView(TemplateView):
    template_name = "clienttemplates/aboutus.html"


class ContactusView(TemplateView):
    template_name = "clienttemplates/contactus.html"


class StudentLoginView(FormView):
    template_name = "clienttemplates/studentlogin.html"
    form_class = StudentLoginForm
    success_url = reverse_lazy("hometuitionapp:home")

    # validating username and password by form_valid method using cleaned_data
    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, 'clienttemplates/studentlogin.html',
                          {
                              "error": "Invalid username or password", "form": form
                          })
        return super().form_valid(form)


class StudentSignupView(FormView):
    template_name = "clienttemplates/studentsignup.html"
    form_class = StudentSignupForm
    success_url = reverse_lazy("hometuitionapp:studentlogin")

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        pword = form.cleaned_data["password"]
        User.objects.create_user(uname, email, pword)
        return super().form_valid(form)


class TeacherLoginView(FormView):
    template_name = "clienttemplates/teacherlogin.html"
    form_class = TeacherLoginForm
    success_url = reverse_lazy("hometuitionapp:home")

    # validating username and password by form_valid method using cleaned_data
    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, 'clienttemplates/teacherlogin.html',
                          {
                              "error": "Invalid username or password", "form": form
                          })
        return super().form_valid(form)


class TeacherSignupView(FormView):
    template_name = "clienttemplates/teachersignup.html"
    form_class = TeacherSignupForm
    success_url = reverse_lazy("hometuitionapp:teacherlogin")

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        pword = form.cleaned_data["password"]
        User.objects.create_user(uname, email, pword)
        return super().form_valid(form)


class LoginView(TemplateView):
    template_name = "clienttemplates/login.html"


class AdminHomeView(TemplateView):
    template_name = "admintemplates/adminhome.html"


class AdminHomeTuitionSystemDetailView(DetailView):
    template_name = "admintemplates/adminsystemdetail.html"
    model = HomeTuitionSystem
    # this context_object_name is used to display data for eg{{systemdetail.name}} will display name of the system
    context_object_name = "systemdetail"


class AdminHomeTuitionSystemUpdateView(UpdateView):
    template_name = "admintemplates/adminsystemupdate.html"
    form_class = HomeTuitionSystemForm
    success_url = reverse_lazy("hometuitionapp:adminhome")
    model = HomeTuitionSystem
