from django.contrib.admin import TabularInline
from users.choices import UserRole
from .inlines import StudentProfileInline, TeacherProfileInline

PROFILE_INLINE_BY_ROLE = {
    UserRole.STUDENT: StudentProfileInline,
    UserRole.TEACHER: TeacherProfileInline,
}


def get_inline_by_role(role: str) -> TabularInline | None:
    return PROFILE_INLINE_BY_ROLE.get(role)
