from typing import Callable
from django.db.models import Model
from abc import ABC


class PermissionProvider(ABC):
    model: Model = None

    def __init__(self):
        self.validate_model()
        self.permission_funcs = self.get_permission_funcs()

    def get_permission_funcs(self) -> list[Callable]:
        return []

    def validate_model(self):
        if self.model is None:
            raise NotImplementedError()

    def get_permissions(self) -> list[str]:
        if not self.permission_funcs:
            raise NotImplementedError()
        permissions = []
        for permission_func in self.permission_funcs:
            permissions.append(permission_func())
        return permissions
