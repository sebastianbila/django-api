from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel

UserModel = get_user_model()


class EmailModelBackend(ModelBackend):
    def authenticate(self, request, username_or_email=None, password=None, **kwargs):
        if "@" in username_or_email:
            kwargs = {'email': username_or_email}
        else:
            kwargs = {'username': username_or_email}
        try:
            user = UserModel.objects.get(**kwargs)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                request.user = user

                return user
        return None
