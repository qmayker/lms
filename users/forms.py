from django import forms
from django.contrib.auth.forms import UserCreationForm as CreationForm

from .choices import UserRole
from .models import User


class UserCreationForm(CreationForm):
    role = forms.ChoiceField(choices=UserRole.choices)

    class Meta(CreationForm.Meta):
        model = User
        fields = CreationForm.Meta.fields + ("email",)

    def __init__(self, *args, roles: list[tuple[str]], **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["role"].choices = roles
        self._delete_help_texts()

    def _delete_help_texts(self):
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
        self.fields["username"].help_text = None
