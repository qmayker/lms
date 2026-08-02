from .base import BaseGroupUserViewService
from .registry import GroupViewRegistry
from .student import GroupStudentViewService
from .teacher import GroupTeacherViewService

group_view_registry = GroupViewRegistry()

group_view_registry.register([GroupTeacherViewService, GroupStudentViewService])

__all__ = [
    "BaseGroupUserViewService",
    "GroupStudentViewService",
    "GroupTeacherViewService",
    "GroupViewRegistry",
    "group_view_registry",
]
