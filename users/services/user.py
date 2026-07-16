from users.choices import UserRole
from users.exceptions import InvalidRoleError
from users.models import Profile, User
from users.types.profiles import ProfileData, StudentProfileData, TeacherProfileData
from .profiles import create_profile


class UserService:
    profile_datas: dict[UserRole, type[ProfileData]] = {
        UserRole.STUDENT: StudentProfileData,
        UserRole.TEACHER: TeacherProfileData,
    }

    def __init__(self, user: User):
        self.user = user

    @property
    def role(self):
        return self.user.role

    @property
    def profile_data_class(self) -> type[ProfileData]:
        try:
            profile_data_class = self.profile_datas[self.role]
        except KeyError:
            raise InvalidRoleError()
        return profile_data_class

    def build_null_profile_data(self) -> ProfileData:
        return self.profile_data_class(user_id=self.user.id)

    def create_profile(self, profile_data: ProfileData) -> Profile:
        if type(profile_data) is not self.profile_data_class:
            raise InvalidRoleError()
        return create_profile(data=profile_data)
