from django.db.models import TextChoices


class UserRole(TextChoices):
    STUDENT = "student", "Student"
    TEACHER = "teacher", "Teacher"
