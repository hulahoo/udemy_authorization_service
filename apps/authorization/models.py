from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.authorization.manager import CustomUserManager
from commons.constants import MENTOR, ADMIN, USER


class CustomUser(AbstractUser):

    USER_TYPE = (
        (MENTOR, "Mentor"),
        (ADMIN, "Admin"),
        (USER, "User")
    )

    is_mentor = models.BooleanField(
        default=False,
        hepl_text=_(
            "Поле для указания, являеться ли пользователь ментором"
        )
    )
    user_type = models.CharField(
        choices=USER_TYPE,
        default=USER,
        max_length=15,
        hepl_text=_(
            "Поле для обозначения типа пользователя"
        )
    )
    activation_code = models.CharField()

    objects = CustomUserManager()
