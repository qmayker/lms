from typing import ClassVar

from users.choices import UserRole
from users.services.roles import RoleRegistry
from users.types.profiles import ProfileData

from .create import ProfileCreateService


class ProfileCreateRegistry(RoleRegistry[type[ProfileCreateService]]):
    DATA: ClassVar = {}

    def create(self, data: ProfileData, role: UserRole, user_id: int):
        service = self.get_by_role(role)(user_id=user_id)
        service.create(data=data)
