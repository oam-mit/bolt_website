from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name='blog'


urlpatterns=[
    path("",views.index,name="index"),
    path("profile",views.profile,name="profile"),
    path("action/<int:action>/",views.action,name="action"),
    path('status',views.status,name="status"),
    path('bulb_status/',views.bulb_status,name="bulb_status"),
]