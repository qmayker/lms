from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.views.decorators.debug import sensitive_variables

UserModel = get_user_model()


class EmailLoginForm(AuthenticationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    def __init__(self, request=..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.email_field = UserModel._meta.get_field(UserModel.EMAIL_FIELD)
        
    @sensitive_variables()
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"username": self.email_field.verbose_name},
        )
