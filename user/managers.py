from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email=None, password=None):
        if not password:
            raise ValueError("Password Error")

        user = self.model(
            phone_number=phone_number,
            email=email,
        )
        user.set_password(password)  # change password to hash
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None,):
        user = self.create_user(
            phone_number=phone_number,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    # def get_by_natural_key(self, phone_number):
    #     return self.get(
    #         models.Q(phone_number__iexact=phoe)
    #     )
