from users.choices import UserRole

from .base import BaseGroupUserViewService


class GroupStudentViewService(BaseGroupUserViewService):
    role = UserRole.STUDENT

    def filter_for_user(self, qs):
        return qs.filter(students=self.user.studentprofile)
