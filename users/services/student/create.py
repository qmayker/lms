from users.choices import UserRole
from users.models import StudentProfile
from users.services.profile import ProfileCreateService
from users.services.user import RoleUserCreateService


class StudentUserCreateService(RoleUserCreateService):
    role = UserRole.STUDENT
    model = StudentProfile


class StudentProfileCreateService(ProfileCreateService):
    role = UserRole.STUDENT
    model = StudentProfile
