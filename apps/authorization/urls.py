from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

from apps.authorization.views import (
    RegistrationView, ForgotPasswordView
)

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="registration"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh-token/", TokenRefreshView.as_view(), name="token-refresh"),
    path(
        "forgot-password/", ForgotPasswordView.as_view(),
        name="forgot-password"
    )
]
