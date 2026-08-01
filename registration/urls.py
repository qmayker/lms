from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import UserLoginView

app_name = "registration"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
