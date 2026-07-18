from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import UserRole

# Create your models here.


class User(AbstractUser):
    role = models.CharField(choices=UserRole.choices, default=UserRole.STUDENT)

    class Meta:
        indexes = [models.Index(fields=["role"])]


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
