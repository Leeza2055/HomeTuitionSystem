from django.urls import path
from .views import *
app_name = 'hometuitionapp'
urlpatterns = [
    # client side
    path('', HomeView.as_view(), name="home"),
    path("aboutus/", AboutusView.as_view(), name="aboutus"),
    path("contactus/", ContactusView.as_view(), name="contactus"),
    path('login/', LoginView.as_view(), name='login'),
    path('student/login/', StudentLoginView.as_view(), name="studentlogin"),
    path('student/register/', StudentRegisterView.as_view(), name="studentregister"),
    path('teacher/login/', TeacherLoginView.as_view(), name="teacherlogin"),
    path('teacher/register/', TeacherRegisterView.as_view(), name="teacherregister"),
    path("search/", SearchView.as_view(), name="search"),
    path('logout/', LogoutView.as_view(), name="logout"),





    # admin side
    path('system_admin/', AdminHomeView.as_view(), name="adminhome"),
    path('adminlogin/', AdminLoginView.as_view(), name="adminlogin"),
    path('system_admin/hometuitionsystem/<int:pk>/detail/',
         AdminHomeTuitionSystemDetailView.as_view(), name="adminsystemdetail"),
    path('system_admin/hometuitionsystem/<int:pk>/update/',
         AdminHomeTuitionSystemUpdateView.as_view(), name="adminsystemupdate"),
    path('system_admin/course/list/',
         AdminCourseListView.as_view(), name="admincourselist"),
    path('system_admin/course/create/',
         AdminCourseCreateView.as_view(), name="admincoursecreate"),
    path('system_admin/course/<int:pk>/update/',
         AdminCourseUpdateView.as_view(), name="admincourseupdate"),
    path('system_admin/course/<int:pk>/delete/',
         AdminCourseDeleteView.as_view(), name="admincoursedelete"),
    path('system_admin/subject/list/',
         AdminSubjectListView.as_view(), name="adminsubjectlist"),
    path('system_admin/course/create/',
         AdminSubjectCreateView.as_view(), name="adminsubjectcreate"),
    path('system_admin/subject/<int:pk>/update/',
         AdminSubjectUpdateView.as_view(), name="adminsubjectupdate"),
    path('system_admin/subject/<int:pk>/delete/',
         AdminSubjectDeleteView.as_view(), name="adminsubjectdelete"),
    path('system_admin/student/list/',
         AdminStudentListView.as_view(), name="adminstudentlist"),

    path('system_admin/student/<int:pk>/detail/',
         AdminStudentDetailView.as_view(), name="adminstudentdetail"),

    path('system_admin/student/<int:pk>/update/',
         AdminStudentUpdateView.as_view(), name="adminstudentupdate"),
    path('system_admin/student/<int:pk>/delete/',
         AdminStudentDeleteView.as_view(), name="adminstudentdelete"),
    path('system_admin/teacher/list/',
         AdminTeacherListView.as_view(), name="adminteacherlist"),
    
    path('system_admin/teacher/<int:pk>/detail/',
         AdminTeacherDetailView.as_view(), name="adminteacherdetail"),

    path('system_admin/teacher/<int:pk>/update',
         AdminTeacherUpdateView.as_view(), name="adminteacherupdate"),
    path('system_admin/teacher/<int:pk>delete',
         AdminTeacherDeleteView.as_view(), name="adminteacherdelete")





]
