from django.urls import path
from .views import *
app_name = 'hometuitionapp'
urlpatterns = [
    # client side
    path('', HomeView.as_view(), name="home"),
    path("aboutus/", AboutusView.as_view(), name="aboutus"),
    path("contactus/", ContactusView.as_view(), name="contactus"),
    # path('login/', LoginView.as_view(), name='login'),
    # path('student/login/', StudentLoginView.as_view(), name="studentlogin"),
    # path('student/signup/', StudentSignupView.as_view(), name="studentsignup"),
    # path('teacher/login/', TeacherLoginView.as_view(), name="teacherlogin"),
    # path('teacher/signup/', TeacherSignupView.as_view(), name="teachersignup"),
    # path('teacher/add/profile/', TeacherProfileView.as_view(), name="teacherprofile"),
    # path('teacher/register/', TeacherRegisterView.as_view(), name="teacherregister"),
    # path('logout/', LogoutView.as_view(), name="logout"),





    # admin side
    # path('system_admin/', AdminHomeView.as_view(), name="adminhome"),
    # # path('adminlogin/',AdminLoginView.as_view(), name="adminlogin"),
    # path('system_admin/hometuitionsystem/<int:pk>/detail/',
    #      AdminHomeTuitionSystemDetailView.as_view(), name="adminsystemdetail"),
    # path('system_admin/hometuitionsystem/<int:pk>/update/',
    #      AdminHomeTuitionSystemUpdateView.as_view(), name="adminsystemupdate"),
    # path('system_admin/teacher/list/', AdminTeacherListView.as_view(), name="adminteacherlist"),
    # path('system_admin/teacher/<int:pk>/update', AdminTeacherUpdateView.as_view(),name="adminteacherupdate"),
    # path('system_admin/teacher/<int:pk>delete',AdminTeacherDeleteView.as_view(), name="adminteacherdelete")





]
