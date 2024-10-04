from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, contact, signup
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("signup/", signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(
        authentication_form=LoginForm, template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(
        template_name="core/logout.html"), name="logout")
]
