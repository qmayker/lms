from django.db.models import Model

from .base import PermissionProvider


class CreatePermissionProvider(PermissionProvider):
    @classmethod
    def create_permission_func(cls, model: Model):
        data = cls.get_model_info(model=model)
        return f"{data.app_label}.add_{data.model_name}"

    @classmethod
    def get_permission_funcs(cls):
        return [cls.create_permission_func]
