from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

UserModel = get_user_model()


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return
        if not user.check_password(password):
            return
        return user

    def get_user(self, user_id):
        return UserModel.objects.filter(id=user_id).first()
