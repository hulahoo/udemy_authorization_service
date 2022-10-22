def validate_email(*, email) -> bool:
    if not email:
        raise ValueError(
            "Пустой емайл"
        )
    return email


def validate_password(*, password, password_confirmation):
    if password != password_confirmation:
        return False
    return True
