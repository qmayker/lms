from django.contrib.auth.views import LoginView

from .forms import EmailLoginForm

# Create your views here.


class UserLoginView(LoginView):
    form_class = EmailLoginForm

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)