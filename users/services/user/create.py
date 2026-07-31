from core.services import BaseCreateService

from users.models import User


class RoleUserCreateService(BaseCreateService):
    model = User
