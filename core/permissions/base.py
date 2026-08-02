from abc import ABC, abstractmethod
from collections.abc import Callable

from core.types import ModelPermissionData
from django.db.models import Model


class PermissionProvider(ABC):
    @classmethod
    @abstractmethod
    def get_permission_funcs(cls) -> list[Callable]: ...

    @classmethod
    def get_permissions(cls, models: list[type[Model]]) -> list[str]:
        permissions = []
        for model in models:
            for permission_func in cls.get_permission_funcs():
                permissions.append(permission_func(model))
        return permissions

    @classmethod
    def get_permission(cls, data: ModelPermissionData, prefix: str):
        return f"{data.app_label}.{prefix}_{data.model_name}"

    @classmethod
    def get_mro_permissions(cls, mro: tuple[type]):
        models = cls.get_models(mro=mro)
        return cls.get_permissions(models=models)

    @staticmethod
    def get_models(mro: tuple[type]) -> list[type[Model]]:
        models: list[Model] = []
        for base in reversed(mro):
            model = base.__dict__.get("model", None)
            if model is None:
                continue
            if model in models:
                continue
            models.append(model)
        if not models:
            raise NotImplementedError()
        return models

    @staticmethod
    def get_model_info(model: Model) -> ModelPermissionData:
        return ModelPermissionData(
            app_label=model._meta.app_label, model_name=model._meta.model_name.lower()
        )
