from typing import ClassVar

from users.services import RoleRegistry

from .base import BaseGroupUserViewService

type GroupViewService = type[BaseGroupUserViewService]


class GroupViewRegistry(RoleRegistry[GroupViewService]):
    DATA: ClassVar = {}
