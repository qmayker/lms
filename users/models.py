from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import UserRole
from .validators import UsernameValidator

# Create your models here.


class User(AbstractUser):
    role = models.CharField(choices=UserRole.choices, default=UserRole.STUDENT)
    email = models.EmailField(blank=False, null=False)

    REQUIRED_FIELDS = ["email"]  # noqa: RUF012
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[UsernameValidator()],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    class Meta:
        indexes = [models.Index(fields=["role"])]  # noqa: RUF012
        constraints = [  # noqa: RUF012
            models.constraints.UniqueConstraint(
                fields=["email"], name="%(app_label)s_%(class)s_email_unique"
            )
        ]


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="%(class)s"
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement build_name()"
        )


class StudentProfile(Profile):
    def __str__(self):
        return f"Student {self.user.username}"


class TeacherProfile(Profile):
    def __str__(self):
        return f"Teacher {self.user.username}"
