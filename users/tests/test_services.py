from django.test import TestCase
from users.services.user import UserService
from users.models import User, StudentProfile, TeacherProfile
from users.choices import UserRole
from users.types.profiles import StudentProfileData, TeacherProfileData, ProfileData
from core.exceptions import InvalidRoleError


class UserServiceTest(TestCase):
    def setUp(self):
        self.student = User.objects.create(username="student", role=UserRole.STUDENT)
        self.teacher = User.objects.create(username="teacher", role=UserRole.TEACHER)
        self.unknown = User.objects.create(username="unknown", role="unknown")

    def _test_profile_data_class(self, user: User, profile_type: type[ProfileData]):
        service = UserService(user=user)
        self.assertEqual(service.profile_data_class, profile_type)

    def test_student_profile_data_class(self):
        self._test_profile_data_class(
            user=self.student, profile_type=StudentProfileData
        )

    def test_teacher_profile_data_class(self):
        self._test_profile_data_class(
            user=self.teacher, profile_type=TeacherProfileData
        )

    def test_unknown_profile_data_class(self):
        service = UserService(user=self.unknown)
        with self.assertRaises(InvalidRoleError):
            service.profile_data_class

    def test_student_create_profile(self):
        service = UserService(user=self.student)
        data = StudentProfileData(user_id=self.student.id)
        profile = service.create_profile(profile_data=data)
        self.assertEqual(profile.user, self.student)
        self.assertEqual(StudentProfile.objects.get(user=self.student), profile)

    def test_teacher_create_profile(self):
        service = UserService(user=self.teacher)
        data = TeacherProfileData(user_id=self.teacher.id)
        profile = service.create_profile(profile_data=data)
        self.assertEqual(profile.user, self.teacher)
        self.assertEqual(TeacherProfile.objects.get(user=self.teacher), profile)

    def test_invalid_create_profile(self):
        service = UserService(user=self.teacher)
        data = StudentProfileData(user_id=self.student.id)
        with self.assertRaises(InvalidRoleError):
            service.create_profile(profile_data=data)
