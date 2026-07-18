from typing import Sequence

from django.contrib import admin

from .models import Group, GroupCounter
from .services.group import GroupCreationService


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "teacher", "created")
    search_fields = ("name",)
    filter_horizontal = ("students",)
    list_filter = ("created",)
    AUTO_GENERATED_FIELDS = ("name",)

    def save_model(self, request, obj: Group, form, change):
        service = GroupCreationService(group=obj)
        service.assign_name()
        service.save()

    @staticmethod
    def _merge_field_names(
        existing_fields: tuple[str], fields_to_add: tuple[str]
    ) -> list[str]:
        existing_fields += fields_to_add
        return list(set(existing_fields))

    def get_exclude(self, request, obj=None):
        exclude = super().get_exclude(request, obj) or ()
        if not obj:
            return self._merge_field_names(exclude, self.AUTO_GENERATED_FIELDS)
        return exclude

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj) or ()
        if obj:
            return self._merge_field_names(readonly_fields, self.AUTO_GENERATED_FIELDS)
        return readonly_fields


@admin.register(GroupCounter)
class GroupCounterAdmin(admin.ModelAdmin):
    list_display = ("prefix", "order")
    search_fields = ("prefix",)
    list_filter = ("prefix",)
