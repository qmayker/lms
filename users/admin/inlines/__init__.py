from .profile import StudentProfileInline, TeacherProfileInline
from .registry import RoleInlineRegistry

inline_registry = RoleInlineRegistry()
inline_registry.register(role_cls_list=[StudentProfileInline, TeacherProfileInline])

__all__ = ['inline_registry']
