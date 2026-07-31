from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.transaction import atomic

from users.forms import UserCreationForm
from users.models import StudentProfile, TeacherProfile, User
from users.services import profile_create_register, role_user_create_register
from users.types.profiles import ProfileData

from .inlines import inline_registry

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    fieldsets = UserAdmin.fieldsets + (("additional_info", {"fields": ("role",)}),)
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "role",
                    "username",
                    "password1",
                    "password2",
                )
            },
        ),
    )

    def get_form(self, request, obj=..., **kwargs):
        Form = super().get_form(request, obj, **kwargs)
        if not obj:
            roles = role_user_create_register.get_available_roles(user=request.user)

            class WrappedForm(Form):
                def __init__(self, *args, **kwargs):
                    super().__init__(
                        *args,
                        roles=roles,
                        **kwargs,
                    )

            return WrappedForm
        return Form

    @atomic
    def save_model(self, request, obj: User, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            service = profile_create_register.get_by_role(role=obj.role)()
            service.create(data=ProfileData(user_id=obj.id))

    def get_inlines(self, request, obj: User | None):
        inlines = super().get_inlines(request, obj)
        if not obj:
            return inlines
        inlines += (inline_registry.get_inlines(obj=obj),)
        return inlines


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username", "user__email")


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user__username", "user__email")
