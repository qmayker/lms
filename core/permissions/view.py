from django.db.models import Model

from .base import PermissionProvider


class ViewPermissionProvider(PermissionProvider):
    @classmethod
    def get_view_permission(cls, model: Model):
        data = cls.get_model_info(model=model)
        return cls.get_permission(data=data, prefix="view")

    @classmethod
    def get_permission_funcs(cls):
        return [cls.get_view_permission]
