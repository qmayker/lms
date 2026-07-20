from abc import ABC
from django.db.models import Model
from .base import PermissionProvider


class CreatePermissionProvider(PermissionProvider, ABC):
    def __init__(self):
        super().__init__()

    def create_permission_func(model: Model):
        return f"add_{model._meta.model_name.lower()}"
