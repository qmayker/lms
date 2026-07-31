from typing import ClassVar

from django.contrib.admin.options import InlineModelAdmin

from users.models import User
from users.services import RoleRegistry


class RoleInlineRegistry(RoleRegistry[InlineModelAdmin]):
    DATA: ClassVar = {}

    def get_inlines(self, obj: User) -> tuple[InlineModelAdmin]:
        return self.get_by_role(role=obj.role)
