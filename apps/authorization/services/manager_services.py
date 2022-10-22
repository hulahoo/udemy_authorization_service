def create_user(
    user_model,
    *,
    last_name: str,
    first_name: str,
    password: str,
    email: str,
    **extra_fields
):
    user = user_model(
        last_name=last_name,
        email=email,
        first_name=first_name,
        **extra_fields
    )
    user.set_password(password=password)
    return user


def create_admin(
    user_model,
    *,
    last_name: str,
    first_name: str,
    password: str,
    email: str,
    **extra_fields
):
    user = user_model(
        last_name=last_name,
        email=email,
        first_name=first_name,
        **extra_fields
    )
    user.set_password(password=password)
    user.is_active = True
    user.is_staff = True
    return user


def create_mentor(
    user_model,
    *,
    last_name: str,
    first_name: str,
    password: str,
    email: str,
    **extra_fields
):
    user = user_model(
        last_name=last_name,
        email=email,
        first_name=first_name,
        **extra_fields
    )
    user.set_password(password=password)
    user.is_mentor = True
    return user
