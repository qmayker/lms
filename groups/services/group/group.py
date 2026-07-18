from django.utils import timezone

from groups.models import Group
from .counter import get_order


class GroupCreationService:
    model = Group

    def __init__(self, group: Group):
        self.group = group

    def get_prefix(self) -> str:
        date = timezone.now().strftime("%y%m%d")
        course_name = self.group.course.name
        return f"{course_name} {date}"

    def build_name(self, prefix: str, order: int) -> str:
        if order == 1:
            return prefix
        return f"{prefix} - {order}"

    def set_name(self, name: str) -> None:
        self.group.name = name

    def save(self) -> None:
        self.group.save()

    def assign_name(self) -> str:
        prefix = self.get_prefix()
        name = self.build_name(prefix=prefix, order=get_order(prefix=prefix))
        self.set_name(name=name)
        return name
