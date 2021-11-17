# region				-----External Imports-----
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models
# endregion

# region				-----Internal Imports-----
from .managers import CustomAccountManager
from .choices import sexes
# endregion


class User(AbstractBaseUser, PermissionsMixin):
    # region       -----Private Information-----
    password = models.CharField(max_length=255,
                                blank=False,
                                null=True,
                                verbose_name="Password")

    is_active = models.BooleanField(default=True,
                                    verbose_name="Is active")

    is_staff = models.BooleanField(default=False,
                                   verbose_name="Is staff")
    # endregion

    # region           -----Information-----
    first_name = models.CharField(max_length=255,
                                  blank=False,
                                  null=False,
                                  verbose_name="First name")

    second_name = models.CharField(max_length=255,
                                   blank=True,
                                   null=True,
                                   verbose_name="Second name")

    email = models.CharField(max_length=255,
                             blank=False,
                             null=False,
                             unique=True,
                             verbose_name="Email")

    sex = models.PositiveSmallIntegerField(blank=False,
                                           null=True,
                                           choices=sexes,
                                           default=0,
                                           verbose_name="Sex")

    about = models.TextField(blank=False,
                             null=True,
                             verbose_name="About")
    # endregion

    # region              -----Metas-----
    USERNAME_FIELD = "email"
    # endregion

    # region         -----Default Methods-----
    def __str__(self) -> str:
        return self.email
    # endregion

    # region             -----Manager-----
    objects = CustomAccountManager()
    # endregion
