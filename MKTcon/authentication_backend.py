from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .ldap import get_LDAP_user


class AuthenticationBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        # Get the user information from the LDAP if he can be authenticated
        if get_LDAP_user(username, password) is None:
            return None

        try:
            user = User.objects.get(username=username)
            print(user)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = False
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
