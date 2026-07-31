from users.choices import UserRole
from users.models import TeacherProfile
from users.services.profile import ProfileCreateService
from users.services.user import RoleUserCreateService


class TeacherUserCreateService(RoleUserCreateService):
    role = UserRole.TEACHER
    model = TeacherProfile


class TeacherProfileCreateService(ProfileCreateService):
    role = UserRole.TEACHER
    model = TeacherProfile
