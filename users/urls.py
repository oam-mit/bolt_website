from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as user_views


from . import views

app_name="users"

urlpatterns=[
    path("",user_views.LoginView.as_view(template_name="users/login.html",redirect_authenticated_user=True),name="login"),
    path("logout",user_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
    path("register",views.register,name="register"),
    path("password-reset/",user_views.PasswordResetView.as_view(template_name="users/reset.html"),name="reset"),
    path("feedback",views.feedback,name="feedback"),
]