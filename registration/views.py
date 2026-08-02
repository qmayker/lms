from django.contrib.auth.views import LoginView

from .forms import EmailLoginForm

# Create your views here.


class UserLoginView(LoginView):
    form_class = EmailLoginForm