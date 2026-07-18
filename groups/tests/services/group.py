from django.test import TestCase
from datetime import datetime
from unittest.mock import patch
from groups.services.group import GroupCreationService, get_order
from groups.models import Group, GroupCounter
from users.models import User, UserRole, TeacherProfile, StudentProfile
from courses.models import Course


class TestGroupService(TestCase):
    def setUp(self):
        teacher_user = User.objects.create(username="qmayker", role=UserRole.TEACHER)
        teacher_profile = TeacherProfile.objects.create(user=teacher_user)

        self.course = Course.objects.create(
            name="Test Course", author=teacher_user, description="test"
        )
        self.group = Group(teacher=teacher_profile, course=self.course)
        self.service = GroupCreationService(group=self.group)

        self.date = datetime(year=2026, month=7, day=18)
        self.prefix = self.date.strftime("%y%m%d")

    def test_build_name(self):
        self.assertEqual(
            self.service.build_name(prefix=self.prefix, order=1), self.prefix
        )
        self.assertEqual(
            self.service.build_name(prefix=self.prefix, order=2), f"{self.prefix} - {2}"
        )

    @patch("groups.services.group.group.timezone.now")
    def test_get_prefix(self, mock_now):
        mock_now.return_value = self.date
        prefix = self.service.get_prefix()
        expected_prefix = f"{self.course.name} {self.prefix}"
        self.assertEqual(prefix, expected_prefix)

    def test_get_order_create(self):
        self.assertEqual(get_order(prefix=self.prefix), 1)
        self.assertEqual(GroupCounter.objects.get(prefix=self.prefix).order, 2)

    def test_get_order_update(self):
        start_order = 2
        GroupCounter.objects.create(prefix=self.prefix, order=start_order)

        self.assertEqual(get_order(prefix=self.prefix), start_order)
        self.assertEqual(
            GroupCounter.objects.get(prefix=self.prefix).order, start_order + 1
        )

    def test_get_order_multiple_calls(self):
        self.assertEqual(get_order(self.prefix), 1)
        self.assertEqual(get_order(self.prefix), 2)
        self.assertEqual(get_order(self.prefix), 3)

        self.assertEqual(
            GroupCounter.objects.get(prefix=self.prefix).order,
            4,
        )
