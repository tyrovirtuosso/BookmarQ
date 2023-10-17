from django.contrib import admin
from django.urls import path, include
from users.views import login_request, login_view
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),    
    path("accounts/login/", login_request, name='account_login'),
    path("accounts/signup/", login_request, name='account_signup'),
    path("accounts/login/link/", login_view, name='login_link'),
    path("accounts/", include("allauth.urls")), 
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
