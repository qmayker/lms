from abc import ABC
from typing import ClassVar
from dataclasses import dataclass
from users.models import Profile, StudentProfile, TeacherProfile


@dataclass
class ProfileData(ABC):
    user_id: int
    profile: ClassVar[type[Profile]]


@dataclass
class StudentProfileData(ProfileData):
    profile = StudentProfile


@dataclass
class TeacherProfileData(ProfileData):
    profile = TeacherProfile
