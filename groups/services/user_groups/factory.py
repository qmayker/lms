from users.models import User
from users.choices import UserRole
from core.exceptions import InvalidRoleError
from . import StudentGroupService, TeacherGroupService, BaseUserGroupService

SERVICES_BY_ROLE = {
    UserRole.STUDENT: StudentGroupService,
    UserRole.TEACHER: TeacherGroupService,
}


def get_by_user_role(user: User) -> type[BaseUserGroupService]:
    role = SERVICES_BY_ROLE.get(user.role)
    if not role:
        raise InvalidRoleError()
    return role
