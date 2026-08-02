from core.services import BaseViewService
from groups.models import Group
from users.models import User


class BaseGroupUserViewService(BaseViewService):
    model = Group

    def __init__(self, user: User):
        self.user = user
