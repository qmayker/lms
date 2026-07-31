from django.urls import path

from .views import UserCreationView, UserDetailView

app_name = "users"

urlpatterns = [
    path("create/", UserCreationView.as_view(), name="user-create"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
