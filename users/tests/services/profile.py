from django.contrib.auth.models import Permission
from django.test import TestCase

from users.choices import UserRole
from users.models import StudentProfile, User
from users.services import (
    StudentProfileCreateService,
    TeacherProfileCreateService,
)
from users.types.profiles import ProfileData


class ProfileCreateTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create(username="admin")
        permissions = Permission.objects.filter(codename__in=["add_studentprofile"])
        self.admin.user_permissions.set(permissions)

        self.student = User.objects.create(username="student", role=UserRole.STUDENT)
        self.teacher = User.objects.create(username="teacher", role=UserRole.TEACHER)

    def test_can_create(self):
        cases = [
            (StudentProfileCreateService, True),
            (TeacherProfileCreateService, False),
        ]
        for service, expected in cases:
            with self.subTest(service=service):
                self.assertEqual(service(user_id=self.admin.id).can_create(user=self.admin), expected)

    def test_create(self):
        student_profile = StudentProfileCreateService(user_id=self.student.id).create(
            ProfileData()
        )
        self.assertIsInstance(student_profile, StudentProfile)
        self.assertEqual(student_profile.user, self.student)
        self.assertEqual(
            StudentProfile.objects.get(user_id=self.student.id), student_profile
        )
