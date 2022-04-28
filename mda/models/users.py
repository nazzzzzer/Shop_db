from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# class Users(models.Model):
#     username = models.CharField(unique=True, max_length=12)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     city = models.CharField(max_length=30)
#     address = models.CharField(max_length=30)

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,

    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=30,
    )
    city = models.CharField(
        verbose_name='city',
        max_length=30,
    )

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email