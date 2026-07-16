from dataclasses import asdict
from users.types.profiles import ProfileData
from users.models import Profile


def create_profile(data: ProfileData) -> Profile:
    return data.profile.objects.create(**asdict(data))
