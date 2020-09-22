from django.urls import path
from .views import *
app_name = 'hometuitionapp'
urlpatterns = [
    # client side
    path('', HomeView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),





    # admin side
    path('system_admin/', AdminHomeView.as_view(), name="adminhome"),
    path('system_admin/hometuitionsystem/<int:pk>/detail/',
         AdminHomeTuitionSystemDetailView.as_view(), name="adminsystemdetail"),
    path('system_admin/hometuitionsystem/<int:pk>/update/',
         AdminHomeTuitionSystemUpdateView.as_view(), name="adminsystemupdate"),





]
