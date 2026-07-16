from users.models import User
from .base import BaseUserGroupService


class TeacherGroupService(BaseUserGroupService):
    def __init__(self, user: User):
        super().__init__(user=user)

    def get_queryset(self, qs):
        return qs.filter(teacher=self.user.teacherprofile)
