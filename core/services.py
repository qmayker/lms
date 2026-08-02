from abc import ABC, abstractmethod

from django.db.models import Model, QuerySet
from users.choices import UserRole
from users.models import User

from .permissions import (
    CreatePermissionProvider,
    PermissionProvider,
    ViewPermissionProvider,
)


class BaseService(ABC):
    role: UserRole = None
    model: type[Model] = None
    provider: PermissionProvider = None

    @classmethod
    def get_permissions(cls):
        return cls.provider.get_mro_permissions(cls.__mro__)

    @classmethod
    def has_permissions(cls, user: User) -> bool:
        return user.has_perms(cls.get_permissions())


class BaseCreateService(BaseService, ABC):
    provider = CreatePermissionProvider

    @abstractmethod
    def create(self, data: object, save: bool): ...


class BaseViewService(BaseService, ABC):
    provider = ViewPermissionProvider

    @abstractmethod
    def filter_for_user(self, qs: QuerySet) -> QuerySet: ...
