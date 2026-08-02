from typing import ClassVar

from users.services.roles import RoleRegistry

from .create import ProfileCreateService


class ProfileCreateRegistry(RoleRegistry[type[ProfileCreateService]]):
    DATA: ClassVar = {}
