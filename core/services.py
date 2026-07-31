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
    def mro(cls):
        return cls.__mro__

    def can_create(self, user: User) -> bool:
        return user.has_perms(self.provider.get_mro_permissions(mro=self.mro()))
