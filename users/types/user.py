from dataclasses import dataclass
from users.choices import UserRole


@dataclass
class UserCreationData:
    username: str
    password: str
    role: UserRole
