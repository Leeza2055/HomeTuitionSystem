from django.views.generic import *
from django.views import generic
from .models import *
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import *
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
# from .tokens import account_activation_token


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


class StudentLoginView(FormView):
    template_name = "clienttemplates/studentlogin.html"
    form_class = StudentLoginForm
    success_url = reverse_lazy("hometuitionapp:studenthome")

    # validating username and password by form_valid method using cleaned_data
    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        user = authenticate(username=uname, password=pword)
        print(user)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, 'clienttemplates/studentlogin.html',
                          {
                              "error": "Invalid username or password", "form": form
                          })
        return super().form_valid(form)


class StudentRegisterView(CreateView):
    template_name = "clienttemplates/studentregister.html"
    form_class = StudentRegisterForm
    success_url = reverse_lazy("hometuitionapp:studentlogin")
    success_message = "Successfully registered"

    def form_valid(self, form):
        uname = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user = User.objects.create_user(uname, email, password)
        form.instance.user = user

        return super().form_valid(form)


class TeacherLoginView(FormView):
    template_name = "clienttemplates/teacherlogin.html"
    form_class = TeacherLoginForm
    success_url = reverse_lazy("hometuitionapp:teacherhome")

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

    # def get_success_url(self):
    #     return reverse_lazy('teacherprofile', kwargs={"pk": self.object.pk})


class TeacherRegisterView(CreateView):
    template_name = "clienttemplates/teacherregister.html"
    form_class = TeacherRegisterForm
    success_url = reverse_lazy("hometuitionapp:teacherlogin")
    success_message = "Successfully registered"

    def form_valid(self, form):
        uname = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user = User.objects.create_user(uname, email, password)
        form.instance.user = user
        return super().form_valid(form)

# class TeacherRegisterView(View):
#     def get(self, request):
#         return render(request, 'clienttemplates/teacherregister.html', {'form': TeacherRegisterForm()})

#     def post(self, request):
#         form = TeacherRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_valid = False
#             user.save()
#             token = user_tokenizer.make_token(user)
#             user_id = urlsafe_base64_encode(force_bytes(user.id))
#             url = 'http://localhost:8000' + reverse('confirm_email',
#                                                     kwargs={'user_id': user_id, 'token': token})
#             message = get_template('clienttemplates/register_email.html').render({
#                 'confirm_url': url
#             })
#             mail = EmailMessage('Email Confirmation', message, to=[
#                                 user.email], from_email=settings.EMAIL_HOST_USER)
#             mail.content_subtype = 'html'
#             mail.send()

#             return render(request, 'clienttemplates/teacherlogin.html',
#                           {
#                               'form': TeacherLoginForm(),
#                               'message': f'A confirmation email has been sent to {user.email}. Please confirm to finish registering'
#                           })
#         return render(request, 'clienttemplates/teacherregister.html', {'form': form})


# class ConfirmRegistrationView(View):
#     def get(self, request, user_id, token):
#         user_id = force_text(urlsafe_base64_decode(user_id))
#         user = User.objects.get(pk=user_id)

#         context = {
#             'form': AuthenticationForm(),
#             'message': 'Registration confirmation error. Please click the reset password to generate a new confirmation email.'
#         }

#         if user and user_tokenizer.check_token(user, token):
#             user.is_valid = True
#             user.save()
#             context['message'] = "Registration complete. Please login"
#         return render(request, 'clienttemplates/teacherlogin', context)


# def teacherregister(request):
#     if request.method == 'POST':
#         form = TeacherRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('clienttemplates/acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(mail_subject, message, to=[to_email])
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = TeacherRegisterForm()
#     return render(request, 'clienttemplates/teacherregister.html', {'form': form})


# def activate(request, uid64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError,User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         # login(request, user)

#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')
# class TeacherRegisterView(View):
#     form_class = TeacherRegisterForm
#     template_name = 'clienttemplates/teacherregister.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():

#             user = form.save(commit=False)
#             user.is_active = False # Deactivate account till it is confirmed
#             user.save()

#             current_site = get_current_site(request)
#             subject = 'Activate Your Account'
#             message = render_to_string('clienttemplates/acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)

#             messages.success(request, ('Please Confirm your email to complete registration.'))

#             return redirect('teacher/login/')

#         return render(request, self.template_name, {'form': form})

# class ActivateAccount(View):

#     def get(self, request, uidb64, token, *args, **kwargs):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None

#         if user is not None and account_activation_token.check_token(user, token):
#             user.is_active = True
#             # user.profile.email_confirmed = True
#             user.save()
#             # login(request, user)
#             messages.success(request, ('Your account have been confirmed.'))
#             return redirect('teacher/login/')
#         else:
#             messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
#             return redirect('teacher/register/')


class StudentHomeView(ListView):
    template_name = "clienttemplates/studenthome.html"

    def get(self, request):
        qs = Teacher.objects.all()
        subject_query = request.GET.get('subject')
        location_query = request.GET.get('location')
        
        if (subject_query != '' and location_query != '') and (subject_query is not None and location_query is not None):
            qset = qs.filter(Q(subject__name__icontains=subject_query), Q(address__icontains=location_query)).distinct()
            print(qset)
            if not qset:
                queryset = qs.order_by("-id")
                messages.error(request, "No results found.")          
                return render(request, "clienttemplates/studenthome.html", {
                    'queryset' : queryset
                })  
            else:
                return render(request, "clienttemplates/studenthome.html", {
                    'queryset' : qset
                })

        elif subject_query != '' and subject_query is not None:
            qset = qs.filter(subject__name__icontains=subject_query) 
            if not qset:
                queryset = qs.order_by("-id")  
                messages.error(request, "No results found.")        
                return render(request, "clienttemplates/studenthome.html", {
                    'queryset' : queryset
                })
            else:
                return render(request, "clienttemplates/studenthome.html", {
                    'queryset' : qset
                })

        elif location_query != '' and location_query is not None:
            qset = qs.filter(address__icontains=location_query)
            if not qset:
                queryset = qs.order_by("-id")
                messages.error(request, "No results found.")          
                return render(request, "clienttemplates/studenthome.html", {
                    'queryset' : queryset
                })  
            else:
                return render(request, "clienttemplates/studenthome.html", {
                    'queryset' : qset
                })

        else:
            qset = qs.order_by("-id")          
            return render(request, "clienttemplates/studenthome.html", {
                'queryset' : qset
            })
        
        


class TeacherHomeView(TemplateView):
    template_name = "clienttemplates/teacherhome.html"


class TeacherProfileView(DetailView):
    template_name = "clienttemplates/teacherprofile.html"
    model = Teacher
    form_class = RatingForm
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher_id = self.kwargs["pk"]
        teacher = Teacher.objects.get(id=teacher_id)

        return context

    def post(self, request, **kwargs):
        url = request.META.get('HTTP_REFERER') #GET last url
        form = self.form_class(request.POST)
        print(self.request)
        if form.is_valid():
            data = Rating() #create relation with model
            data.rate = form.cleaned_data['rate']
            teacher_id = self.kwargs["pk"]
            data.teacher = Teacher.objects.get(id=teacher_id)
            try:
                print(self.request)
                # data.user = User.objects.get(user=self.request.user)
                current_user = request.user
                print(current_user)
                data.user = current_user.id
                print(data.user)
            except:
                print("except")
            # current_user = request.user
            # print(current_user, '\n ++++++++++++++++++++++++')
            # data.user_id = current_user.id
            data.save()
            messages.success(request,"Your review has been sent")
            return HttpResponseRedirect(url)
        else:
            return render(self.request, url)

    # if request.method == 'POST':
    #     form = RateForm(request.POST, i)



# class SearchView(TemplateView):
#     template_name = "clienttemplates/searchresult.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         keyword = self.request.GET["query"]
#         print(keyword, "+++++++++++")
#         teachers = Teacher.object.filter(Q(address__icontains=keyword)
#                                          | Q(subject__icontains=keyword))
#         context["searched_teachers"] = teachers
#         return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


# class AdminRequiredMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_superuser:
#             return redirect("/adminlogin/")
#         return super().dispatch(request, *args, **kwargs)


class AdminHomeView(TemplateView):
    template_name = "admintemplates/adminhome.html"


class AdminLoginView(FormView):
    template_name = "admintemplates/adminlogin.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("hometuitionapp:adminhome")

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, "admintemplates/adminlogin.html",
                          {
                              "error": "Invalid username or password", "form": form
                          })
        return super().form_valid(form)


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


class AdminCourseListView(ListView):
    template_name = "admintemplates/admincourselist.html"
    queryset = Course.objects.all().order_by("-id")
    context_object_name = "courselist"


class AdminCourseCreateView(CreateView):
    template_name = "admintemplates/admincoursecreate.html"
    form_class = CourseForm
    success_url = reverse_lazy("hometuitionapp:admincourselist")


class AdminCourseUpdateView(UpdateView):
    template_name = "admintemplates/admincourseupdate.html"
    form_class = CourseForm
    success_url = reverse_lazy("hometuitionapp:admincourselist")
    model = Course


class AdminCourseDeleteView(DeleteView):
    template_name = "admintemplates/admincoursedelete.html"
    success_url = reverse_lazy("hometuitionapp:admincourselist")
    model = Course


class AdminSubjectListView(ListView):
    template_name = "admintemplates/adminsubjectlist.html"
    queryset = Subject.objects.all().order_by("-id")
    context_object_name = "subjectlist"


class AdminSubjectCreateView(CreateView):
    template_name = "admintemplates/adminsubjectcreate.html"
    form_class = SubjectForm
    success_url = reverse_lazy("hometuitionapp:adminsubjectlist")


class AdminSubjectUpdateView(UpdateView):
    template_name = "admintemplates/adminsubjectupdate.html"
    form_class = SubjectForm
    success_url = reverse_lazy("hometuitionapp:adminsubjectlist")
    model = Subject


class AdminSubjectDeleteView(DeleteView):
    template_name = "admintemplates/adminsubjectdelete.html"
    success_url = reverse_lazy("hometuitionapp:adminsubjectlist")
    model = Subject


class AdminStudentListView(ListView):
    template_name = "admintemplates/adminstudentlist.html"
    queryset = Student.objects.all().order_by("-id")
    context_object_name = "studentlist"


class AdminStudentDetailView(DetailView):
    template_name = "admintemplates/adminstudentdetail.html"
    model = Student
    context_object_name = "studentdetail"


class AdminStudentUpdateView(UpdateView):
    template_name = "admintemplates/adminstudentupdate.html"
    form_class = StudentRegisterForm
    success_url = reverse_lazy("hometuitionapp:adminstudentlist")
    model = Student


class AdminStudentDeleteView(DeleteView):
    template_name = "admintemplates/adminstudentdelete.html"
    success_url = reverse_lazy("hometuitionapp:adminstudentlist")
    model = Student


class AdminTeacherListView(ListView):
    template_name = "admintemplates/adminteacherlist.html"
    queryset = Teacher.objects.all().order_by("-id")
    context_object_name = "teacherlist"


class AdminTeacherUpdateView(UpdateView):
    template_name = "admintemplates/adminteacherupdate.html"
    form_class = TeacherRegisterForm
    success_url = reverse_lazy("hometuitionapp:adminteacherlist")
    model = Teacher


class AdminTeacherDeleteView(DeleteView):
    template_name = "admintemplates/adminteacherdelete.html"
    success_url = reverse_lazy("hometuitionapp:adminteacherlist")
    model = Teacher


class AdminTeacherDetailView(DetailView):
    template_name = "admintemplates/adminteacherdetail.html"
    model = Teacher
    context_object_name = "teacherdetail"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     teacher_id = self.kwargs["pk"]
    #     teacher = Teacher.objects.get(id=teacher_id)

    #     return context
