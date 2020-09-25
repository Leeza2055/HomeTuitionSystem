from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *


# class TeacherRequiredMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.groups.filter(name="teacher").exists():
#             pass
#         else:
#             return redirect("/login/")
#         return super().dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "clienttemplates/home.html"


class AboutusView(TemplateView):
    template_name = "clienttemplates/aboutus.html"


class ContactusView(TemplateView):
    template_name = "clienttemplates/contactus.html"


class LoginView(TemplateView):
    template_name = "clienttemplates/login.html"


# class StudentLoginView(FormView):
#     template_name = "clienttemplates/studentlogin.html"
#     form_class = StudentLoginForm
#     success_url = reverse_lazy("hometuitionapp:home")

#     # validating username and password by form_valid method using cleaned_data
#     def form_valid(self, form):
#         uname = form.cleaned_data["username"]
#         pword = form.cleaned_data["password"]
#         user = authenticate(username=uname, password=pword)
#         if user is not None:
#             login(self.request, user)
#         else:
#             return render(self.request, 'clienttemplates/studentlogin.html',
#                           {
#                               "error": "Invalid username or password", "form": form
#                           })
#         return super().form_valid(form)


# class StudentSignupView(FormView):
#     template_name = "clienttemplates/studentsignup.html"
#     form_class = StudentSignupForm
#     success_url = reverse_lazy("hometuitionapp:studentlogin")

#     def form_valid(self, form):
#         uname = form.cleaned_data["username"]
#         email = form.cleaned_data["email"]
#         pword = form.cleaned_data["password"]
#         User.objects.create_user(uname, email, pword)
#         return super().form_valid(form)


# class TeacherLoginView(FormView):
#     template_name = "clienttemplates/teacherlogin.html"
#     form_class = TeacherLoginForm
#     success_url = reverse_lazy("hometuitionapp:aboutus")

#     # validating username and password by form_valid method using cleaned_data
#     def form_valid(self, form):
#         uname = form.cleaned_data["username"]
#         pword = form.cleaned_data["password"]
#         user = authenticate(username=uname, password=pword)
#         if user is not None:
#             login(self.request, user)
#         else:
#             return render(self.request, 'clienttemplates/teacherlogin.html',
#                           {
#                               "error": "Invalid username or password", "form": form
#                           })
#         return super().form_valid(form)


# class TeacherSignupView(FormView):
#     template_name = "clienttemplates/teachersignup.html"
#     form_class = TeacherSignupForm
#     success_url = reverse_lazy("hometuitionapp:teacherlogin")

#     def form_valid(self, form):
#         uname = form.cleaned_data["username"]
#         email = form.cleaned_data["email"]
#         pword = form.cleaned_data["password"]
#         user = User.objects.create_user(uname, email, pword)
#         return super().form_valid(form)


# class TeacherProfileView(TemplateView):
#     template_name = "clienttemplates/teacherprofile.html"

# class TeacherRegisterView(CreateView):
#     template_name = "clienttemplates/teacherregister.html"
#     form_class = TeacherSignupForm
#     success_url = reverse_lazy("hometuitionapp:home")
#     success_message = "Successfully registered"

#     def form_valid(self, form):
#         uname = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         email = form.cleaned_data['email']
#         user = User.objects.create_user(uname, email, password)
#         form.instance.user = user

#         return super().form_valid(form)


# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect("/")


# class AdminRequiredMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_superuser:
#             return redirect("/adminlogin/")
#         return super().dispatch(request, *args, **kwargs)


class AdminHomeView(TemplateView):
    template_name = "admintemplates/adminhome.html"


# class AdminLoginView(FormView):
#     template_name = "admintemplates/adminlogin.html"
#     form_class = AdminLoginForm
#     success_url = reverse_lazy("hometuitionapp:adminhome")

#     def form_valid(self, form):
#         uname = form.cleaned_data["username"]
#         pword = form.cleaned_data["password"]
#         user = authenticate(username=uname, password=pword)
#         if user is not None:
#             login(self.request, user)
#         else:
#             return render(self.request, "admintemplates/adminlogin.html",
#                           {
#                               "error": "Invalid username or password", "form": form
#                           })
#         return super().form_valid(form)


# class AdminHomeTuitionSystemDetailView(DetailView):
#     template_name = "admintemplates/adminsystemdetail.html"
#     model = HomeTuitionSystem
#     # this context_object_name is used to display data for eg{{systemdetail.name}} will display name of the system
#     context_object_name = "systemdetail"


# class AdminHomeTuitionSystemUpdateView(UpdateView):
#     template_name = "admintemplates/adminsystemupdate.html"
#     form_class = HomeTuitionSystemForm
#     success_url = reverse_lazy("hometuitionapp:adminhome")
#     model = HomeTuitionSystem


# class AdminTeacherListView(ListView):
#     template_name = "admintemplates/adminteacherlist.html"
#     queryset = Teacher.objects.all().order_by("-id")
#     context_object_name = "teacherlist"


# class AdminTeacherUpdateView(UpdateView):
#     template_name = "admintemplates/adminteacherupdate.html"
#     form_class = TeacherRegisterForm
#     success_url = reverse_lazy("hometuitionapp:adminteacherlist")
#     model = Teacher


# class AdminTeacherDeleteView(DeleteView):
#     template_name = "admintemplates/adminteacherdelete.html"
#     success_url = reverse_lazy("hometuitionapp:adminteacherlist")
#     model = Teacher
