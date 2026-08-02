from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView

from .models import Group
from .services.user_groups import (
    BaseGroupUserViewService,
    group_view_registry,
)


class GroupListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Group
    template_name = "groups/group/list.html"
    permission_required = BaseGroupUserViewService.get_permissions()

    def get(self, request, *args, **kwargs):
        self.service = group_view_registry.get_by_role(request.user.role)(
            user=self.request.user
        )
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return self.service.filter_for_user(qs=qs)
