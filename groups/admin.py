from django.contrib import admin

from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "teacher", "created")
    search_fields = ("name",)
    filter_horizontal = ("students",)
    list_filter = ("created",)
