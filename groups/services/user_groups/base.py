from django.db.models import QuerySet
from abc import ABC, abstractmethod
from groups.models import Group
from users.models import User


class BaseUserGroupService(ABC):
    def __init__(self, user: User):
        self.user = user

    @abstractmethod
    def get_queryset(self, qs: QuerySet[Group]) -> QuerySet: ...
