from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from core.fields import OrderedField
from core.models import TimeTrackModel

# Create your models here.


class Course(TimeTrackModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="courses"
    )
    name = models.CharField()
    description = models.TextField()


class Module(TimeTrackModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    order = OrderedField()
    name = models.CharField()

    class Meta:
        ordering = ["order"]
        indexes = [models.Index(fields=["order"])]


class Content(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, related_name="contents"
    )
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["object_id", "content_type"],
                name="content_object_unique",
            )
        ]


class ContentItem(TimeTrackModel):
    content = GenericRelation(Content)

    class Meta(TimeTrackModel.Meta):
        abstract = True


class TextContent(ContentItem):
    text_content = models.TextField()
