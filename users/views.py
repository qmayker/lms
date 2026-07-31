from django.db.transaction import atomic
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from users.types.profiles import ProfileData

from .forms import UserCreationForm
from .models import User
from .services import profile_create_register, role_user_create_register

# TODO - Login, Profile creation with email, Permissions.


class UserCreationView(CreateView):
    template_name = "users/user/create.html"
    form_class = UserCreationForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["roles"] = role_user_create_register.get_available_roles(
            user=self.request.user
        )
        return kwargs

    @atomic
    def form_valid(self, form: UserCreationForm):
        res = super().form_valid(form)
        profile_create_register.create(
            data=ProfileData(user_id=self.object.id), role=self.object.role
        )
        return res

    def get_success_url(self):
        return reverse("users:user-detail", args=[self.object.id])


class UserDetailView(DetailView):
    model = User
    form_class = UserCreationForm
    template_name = "users/user/detail.html"
