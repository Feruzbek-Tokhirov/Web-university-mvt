from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import user_login, user_logout, user_register


urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("", user_register, name="register")
    # path("login/", LoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
]
