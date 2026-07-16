from users.models import User
from .base import BaseUserGroupService


class StudentGroupService(BaseUserGroupService):
    def __init__(self, user: User):
        super().__init__(user=user)

    def get_queryset(self, qs):
        return qs.filter(students=self.user.studentprofile)
