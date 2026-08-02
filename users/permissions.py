from django.contrib.auth.mixins import PermissionRequiredMixin

from .services import (
    role_user_create_register,
)


class UserCreatePermissionRequiredMixin(PermissionRequiredMixin):
    def has_permission(self):
        if not super().has_permission():
            return False
        return bool(role_user_create_register.get_available_roles(self.request.user))
