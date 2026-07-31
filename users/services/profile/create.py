from abc import ABC
from dataclasses import asdict

from core.services import BaseCreateService
from django.db.models import Model

from users.models import Profile
from users.types.profiles import ProfileData


class ProfileCreateService(BaseCreateService, ABC):
    model: Profile

    def create(self, data: ProfileData, save: bool = True) -> Model:
        obj = self.model(**asdict(data))
        if save:
            obj.save()
        return obj
