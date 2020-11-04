from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url
from .views import *
from . import views
# from .tokens import account_activation_token

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
    path('teacher/register/', TeacherRegisterView.as_view(),
         name="teacherregister"),
    # path('activate/<uid>/<token>/', ActivateAccount.as_view(), name='activate'),
    # url(r'^teacher/register/$', views.teacherregister, name='teacherregister'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path('teacher/home/', TeacherHomeView.as_view(), name="teacherhome"),
    path('student/home/', StudentHomeView.as_view(), name="studenthome"),
    # path('confirm-email/<str:user_id>/<str:token>/',
    #      views.ConfirmRegistrationView.as_view(), name='confirm_email'),
    # path('reset-password/', auth_views.PasswordResetView.as_view(
    #      template_name='clienttemplates/reset_password.html',
    #      html_email_template_name='clienttemplates/reset_password_email.html',
    #      success_url=settings.TEACHER_LOGIN_URL,
    #      token_generator=user_tokenizer),
    #      name='reset_password'),
    # path('reset-password-confirmation/<str:uidb64>/<str:token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='clienttmplates/reset_password_update.html',
    #          post_reset_login=True,
    #          post_reset_login_backend='django.contrib.auth.backends.ModelBackend',
    #          token_generator=user_tokenizer,
    #          success_url=settings.TEACHER_LOGIN_REDIRECT_URL),
    #      name='password_reset_confirm'),
    path('teacher/<int:pk>/profile/',
         TeacherProfileView.as_view(), name="teacherprofile"),
    # path("search/", SearchView.as_view(), name="search"),
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
         AdminTeacherDeleteView.as_view(), name="adminteacherdelete"),
]
