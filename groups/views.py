from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .services.user_groups import (
    get_by_user_role,
)
from .models import Group


class GroupListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Group
    template_name = "groups/group/list.html"
    permission_required = ["groups.view_group"]

    def dispatch(self, request, *args, **kwargs):
        self.service = get_by_user_role(user=request.user)(user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return self.service.get_queryset(qs=qs)
    
# TODO - auto naming group
# TODO - add __str__
