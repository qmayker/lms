from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.transaction import atomic
from users.choices import UserRole
from users.services.user import UserService
from users.models import StudentProfile, TeacherProfile, User
from .utils import get_inline_by_role

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("additional_info", {"fields": ("role",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("role",)}),)

    @atomic
    def save_model(self, request, obj: User, form, change):
        super().save_model(request, obj, form, change)
        service = UserService(user=obj)
        service.create_profile(profile_data=service.build_null_profile_data())

    @staticmethod
    def _get_role(obj: User | None) -> str:
        if obj:
            role = obj.role
        else:
            role = None
        return role

    def get_inlines(self, request, obj: User | None):
        inlines = super().get_inlines(request, obj)
        role = self._get_role(obj=obj)
        role_inline = get_inline_by_role(role=role)
        if role_inline:
            inlines += (role_inline,)
        return inlines


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username", "user__email")


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username", "user__email")
