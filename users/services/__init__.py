from .profile import (
    ProfileCreateRegistry,
    ProfileCreateService,
)
from .roles import RoleRegistry
from .student import StudentProfileCreateService, StudentUserCreateService
from .teacher import TeacherProfileCreateService, TeacherUserCreateService
from .user import (
    RoleUserCreateRegistry,
    RoleUserCreateService,
)

role_user_create_register = RoleUserCreateRegistry()
role_user_create_register.register(
    role_cls_list=[StudentUserCreateService, TeacherUserCreateService]
)

profile_create_register = ProfileCreateRegistry()
profile_create_register.register(
    role_cls_list=[StudentProfileCreateService, TeacherProfileCreateService]
)

__all__ = [
    "ProfileCreateRegistry",
    "ProfileCreateService",
    "RoleRegistry",
    "RoleUserCreateMixin",
    "RoleUserCreateRegistry",
    "RoleUserCreateService",
    "StudentUserCreateService",
    "TeacherUserCreateService",
    "UserCreatePermissionProvider",
    "UserCreateService",
    "profile_create_register",
]
