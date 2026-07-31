from abc import ABC
from dataclasses import asdict

from core.services import BaseCreateService
from django.db.models import Model

from users.models import Profile
from users.types.profiles import ProfileData


class ProfileCreateService(BaseCreateService, ABC):
    model: Profile

    def __init__(self, user_id: int):
        self.user_id = user_id

    def create(self, data: ProfileData, save: bool = True) -> Model:
        obj = self.model(user_id=self.user_id, **asdict(data))
        if save:
            obj.save()
        return obj
