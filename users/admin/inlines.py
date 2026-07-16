from django.contrib import admin
from users.models import StudentProfile, TeacherProfile


class StudentProfileInline(admin.TabularInline):
    model = StudentProfile


class TeacherProfileInline(admin.TabularInline):
    model = TeacherProfile
