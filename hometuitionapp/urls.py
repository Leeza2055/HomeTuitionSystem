from django.urls import path
from .views import *
app_name = 'hometuitionapp'
urlpatterns = [
    # client side
    path('', HomeView.as_view(), name="home"),
    path("aboutus/", AboutusView.as_view(), name="aboutus"),
    path("contactus/", ContactusView.as_view(), name="contactus"),
    path('login/', LoginView.as_view(), name='login'),
    path('studentlogin/', StudentLoginView.as_view(), name="studentlogin"),
    path('studentsignup/', StudentSignupView.as_view(), name="studentsignup"),
    path('teacherlogin/', TeacherLoginView.as_view(), name="teacherlogin"),
    path('teachersignup/', TeacherSignupView.as_view(), name="teachersignup"),





    # admin side
    path('system_admin/', AdminHomeView.as_view(), name="adminhome"),
    # path('adminlogin/',AdminLoginView.as_view(), name="adminlogin"),
    path('system_admin/hometuitionsystem/<int:pk>/detail/',
         AdminHomeTuitionSystemDetailView.as_view(), name="adminsystemdetail"),
    path('system_admin/hometuitionsystem/<int:pk>/update/',
         AdminHomeTuitionSystemUpdateView.as_view(), name="adminsystemupdate"),





]
