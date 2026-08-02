from core.permissions import CreatePermissionProvider
from core.services import BaseService

from users.models import User


class RoleUserCreateService(BaseService):
    model = User
    provider = CreatePermissionProvider
