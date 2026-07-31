from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest


class BaseRoleRequiredMixin:
    role: str = None

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if request.user.role != self.role:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class RoleRequiredMixin(LoginRequiredMixin, BaseRoleRequiredMixin):
    pass
