from django.contrib.auth.base_user import BaseUserManager

from apps.authorization.services.validating import validate_email
from apps.authorization.services.manager_services import (
    create_user, create_admin, create_mentor
)


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        *,
        last_name: str,
        first_name: str,
        password: str,
        email: str,
        **extra_fields
    ):
        email = validate_email(email=email)
        email = self.normalize_email(email=email)
        user = create_user(
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user

    def create_admin(
        self,
        *,
        last_name: str,
        first_name: str,
        password: str,
        email: str,
        **extra_fields
    ):
        email = validate_email(email=email)
        user = create_admin(
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user

    def create_mentor(
        self,
        *,
        last_name: str,
        first_name: str,
        password: str,
        email: str,
        **extra_fields
    ):
        email = validate_email(email=email)
        user = create_mentor(
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user
