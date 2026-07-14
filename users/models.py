from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import TextChoices

# Create your models here.


class User(AbstractUser):
    role = models.CharField(choices=TextChoices)


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student_profile"
    )


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teacher_profile"
    )
