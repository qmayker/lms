from users.choices import UserRole

from .base import BaseGroupUserViewService


class GroupTeacherViewService(BaseGroupUserViewService):
    role = UserRole.TEACHER

    def filter_for_user(self, qs):
        return qs.filter(teacher=self.user.teacherprofile)
