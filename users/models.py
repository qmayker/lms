from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import UserRole

# Create your models here.


class User(AbstractUser):
    role = models.CharField(choices=UserRole.choices, default=UserRole.STUDENT)


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teacher_profile"
    )
