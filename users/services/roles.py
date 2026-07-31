from abc import ABC

from core.exceptions import InvalidRoleError

from users.choices import UserRole


class RoleRegistry[T](ABC):
    DATA: dict[UserRole, T] = None

    def __init__(self):
        self.data_implemented()

    def data_implemented(self):
        if getattr(self, "DATA", None) is None:
            raise NotImplementedError()

    def _register_role(self, role: UserRole, cls: T):
        self.DATA[role] = cls

    def register_role(self, role: UserRole, cls: T) -> None:
        if role in self.DATA:
            raise ValueError(f"{role} was already used")
        self._register_role(role=role, cls=cls)

    def register(self, role_cls_list: list[T]):
        for role_cls in role_cls_list:
            role = getattr(role_cls, "role", None)
            if not role:
                raise NotImplementedError()
            self.register_role(role=role, cls=role_cls)

    def get_by_role(self, role: UserRole) -> T:
        value = self.DATA.get(role)
        if value is None:
            raise InvalidRoleError()
        return value
