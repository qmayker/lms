from typing import ClassVar

from core.exceptions import InvalidRoleError
from django.test import TestCase

from users.choices import UserRole
from users.models import User
from users.services import (
    RoleUserCreateRegistry,
    StudentUserCreateService,
    TeacherUserCreateService,
)
from users.services.roles import RoleRegistry


class TestRegistry(RoleRegistry[type]):
    DATA: ClassVar = {}


class InvalidService: ...


class RegistryTest(TestCase):
    def setUp(self):
        TestRegistry.DATA = {}
        self.registry = TestRegistry()
        self.student_role = UserRole.STUDENT
        self.student_service = StudentUserCreateService
        self.teacher_role = UserRole.TEACHER
        self.teacher_service = TeacherUserCreateService

    def test_get_by_role(self):
        self.registry.DATA[self.student_role] = self.student_service
        self.assertIs(
            self.registry.get_by_role(self.student_role), self.student_service
        )

    def test_invalid_get_by_role(self):
        with self.assertRaises(InvalidRoleError):
            self.registry.get_by_role(self.student_role)

    def test_register_role(self):
        self.registry.register_role(self.student_role, self.student_service)

        self.assertIs(
            self.registry.DATA[self.student_role],
            self.student_service,
        )

    def test_register_role_duplicate(self):
        self.registry.register_role(self.student_role, self.student_service)
        with self.assertRaises(ValueError):
            self.registry.register_role(self.student_role, self.student_service)

    def test_register(self):
        self.registry.register([self.student_service, self.teacher_service])
        self.assertEqual(self.registry.DATA[self.teacher_role], self.teacher_service)
        self.assertEqual(self.registry.DATA[self.student_role], self.student_service)

    def test_invalid_register(self):
        with self.assertRaises(NotImplementedError):
            self.registry.register([InvalidService])


class AllowCreate:
    def has_permissions(self, user):
        return True


class DenyCreate:
    def has_permissions(self, user):
        return False


class RoleUserRegistryTest(TestCase):
    def setUp(self):
        self.registry = RoleUserCreateRegistry()
        self.user = User.objects.create(username="test")

    def test_get_available_roles(self):
        self.registry.DATA = {
            UserRole.STUDENT: AllowCreate,
            UserRole.TEACHER: AllowCreate,
        }
        roles = self.registry.get_available_roles(user=self.user)
        self.assertCountEqual(roles, UserRole.choices)
