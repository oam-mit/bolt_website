"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import settings
from django.conf.urls.static import static

from django.contrib.auth import views as user_views


urlpatterns = [
    #Admininistration urls
    path('admin/', admin.site.urls),

    #Website urls
    path('',include("users.urls")),
    path('user/',include("blog.urls")),

    path("password-reset/confirm/<uidb64>/<token>/",user_views.PasswordResetConfirmView.as_view(template_name="users/reset_confirm.html"),name="password_reset_confirm"),
    path("password-reset/sent/",user_views.PasswordResetDoneView.as_view(template_name="users/reset_sent.html"),name="password_reset_done"),
    path("password-reset/complete/",user_views.PasswordResetCompleteView.as_view(template_name="users/reset_complete.html"),name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
