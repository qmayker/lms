from abc import ABC

from django.db.models import Model
from users.choices import UserRole
from users.models import User

from .permissions import CreatePermissionProvider


class BaseCreateService(ABC):
    provider = CreatePermissionProvider
    model: type[Model] = None
    role: UserRole = None

    @classmethod
    def permissions(cls):
        return cls.provider.get_mro_permissions(cls.__mro__)

    @classmethod
    def can_create(cls, user: User) -> bool:
        return user.has_perms(cls.permissions())
