import email
from typing import Dict

from rest_framework import status
from rest_framework import serializers

from commons.constants import MENTOR, ADMIN
from apps.authorization.services.validating import validate_password
from apps.authorization.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=4, required=True, write_only=True
    )
    password_confirm = serializers.CharField(
        min_length=4, required=True, write_only=True
    )

    class Meta:
        model = CustomUser
        fields = (
            "password", "password_confirm", "user_type",
            "last_name", "first_name", "email"
        )

    def validate(
        self,
        to_validate: Dict[str, str]
    ) -> Dict[str, str]:
        password = to_validate.get("password")
        password_confirm = to_validate.pop("password_confirm")
        is_passwords_same = validate_password(
            password=password,
            password_confirmation=password_confirm
        )
        if not is_passwords_same:
            raise serializers.ValidationError(
                detail="Passwords does not match",
                code=status.HTTP_400_BAD_REQUEST
            )
        return to_validate

    def create(
        self, validated_data: Dict[str, str]
    ) -> CustomUser:
        user_type = validated_data.get("user_type")
        if user_type == MENTOR:
            user = CustomUser.objects.create_mentor(**validated_data)
        elif user_type == ADMIN:
            user = CustomUser.objects.create_admin(**validated_data)
        else:
            user = CustomUser.objects.create_user(**validated_data)
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=4, required=True, write_only=True
    )
    password_confirm = serializers.CharField(
        min_length=4, required=True, write_only=True
    )

    def validate_user(
        self,
        to_validate: Dict[str, str]
    ) -> Dict[str, str]:
        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                detail="User not found",
                code=status.HTTP_400_BAD_REQUEST
            )
        return to_validate

    def validate(
        self,
        to_validate: Dict[str, str]
    ) -> Dict[str, str]:
        password = to_validate.get("password")
        password_confirm = to_validate.pop("password_confirm")
        is_passwords_same = validate_password(
            password=password,
            password_confirmation=password_confirm
        )
        if not is_passwords_same:
            raise serializers.ValidationError(
                detail="Passwords does not match",
                code=status.HTTP_400_BAD_REQUEST
            )
        return to_validate

    def save(self, **kwargs) -> CustomUser:
        password: str = self.validated_data.get("password")
        email: str = self.validated_data.get("email")
        user = CustomUser.objects.get(email=email)
        user.set_password(password=password)
        user.save()
        return user
