from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Course, Module, Content, TextContent


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "created", "edited")
    list_filter = ("author", "created")
    search_fields = ("name", "description", "author__username")
    ordering = ("name",)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "order", "created", "edited")
    list_filter = ("course", "created")
    search_fields = ("name", "course__name")
    ordering = ("course", "order", "name")

    def get_exclude(self, request, obj=None) -> tuple:
        if obj is None:
            return ("order",)
        return ()


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("module", "content_type", "object_id")
    list_filter = ("module", "content_type")
    search_fields = ("module__name", "content_type__model")
    ordering = ("module", "content_type", "object_id")


class ContentInline(GenericTabularInline):
    model = Content
    extra = 0
    max_num = 1
    min_num = 1


@admin.register(TextContent)
class TextContentAdmin(admin.ModelAdmin):
    list_display = ("id", "content__module", "text_content")
    list_filter = ("content__module",)
    search_fields = ("text_content",)
    ordering = ("content__module", "id")
    inlines = [ContentInline]
