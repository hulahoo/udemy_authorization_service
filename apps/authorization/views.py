from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.authorization.serializers import (
    RegistrationSerializer, ForgotPasswordSerializer
)


class RegistrationView(APIView):
    def post(self, request):
        registration_payload = request.data
        serializer = RegistrationSerializer(data=registration_payload)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                data="User created successfully",
                status=status.HTTP_200_OK
            )


class ForgotPasswordView(APIView):
    def post(self, request):
        request_data = request.data
        serializer = ForgotPasswordSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                data="Password changed successfully",
                status=status.HTTP_200_OK
            )
