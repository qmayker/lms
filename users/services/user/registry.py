from typing import ClassVar

from users.choices import UserRole
from users.services.roles import RoleRegistry

from .create import RoleUserCreateService


class RoleUserCreateRegistry(RoleRegistry[type[RoleUserCreateService]]):
    DATA: ClassVar = {}

    def get_available_roles(self, user) -> list[tuple[UserRole, str]]:
        roles = []
        for role, service_type in self.DATA.items():
            service = service_type()
            if not service.can_create(user=user):
                continue
            roles.append((role.value, role.label))
        return roles
