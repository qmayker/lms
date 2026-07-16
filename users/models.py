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


class StudentProfile(Profile): ...


class TeacherProfile(Profile): ...
