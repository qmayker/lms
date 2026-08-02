from django.db.models import Model

from .base import PermissionProvider


class CreatePermissionProvider(PermissionProvider):
    @classmethod
    def get_create_permission(cls, model: Model):
        data = cls.get_model_info(model=model)
        return cls.get_permission(data=data, prefix="add")

    @classmethod
    def get_permission_funcs(cls):
        return [cls.get_create_permission]
