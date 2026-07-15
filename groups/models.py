from django.db import models

# Create your models here.


class Group(models.Model):
    teacher = models.ForeignKey(
        "users.TeacherProfile", on_delete=models.CASCADE, related_name="groups"
    )
    students = models.ManyToManyField("users.StudentProfile", related_name="groups")
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="groups"
    )
    name = models.CharField()
