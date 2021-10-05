from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from .models import MyUser
from django.db.models import Q

class SettingsBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        user= MyUser.objects.get(Q(username=username) | Q(email=username) | Q(phone_number = username))
        try:
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None