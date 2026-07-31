from django.contrib import admin

from users.choices import UserRole
from users.models import StudentProfile, TeacherProfile


class StudentProfileInline(admin.TabularInline):
    model = StudentProfile
    role = UserRole.STUDENT


class TeacherProfileInline(admin.TabularInline):
    model = TeacherProfile
    role = UserRole.TEACHER
