from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import exceptions
from rest_framework import status
from django.conf import settings
import jwt

from users.utils import generate_access_token, generate_refresh_token
from users.serializers import UserSerializer
from users.models import User


class JWTViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["POST"], detail=False, url_path="token", permission_classes=[AllowAny])
    def token(self, request: HttpRequest):
        login = request.data.get("login")
        password = request.data.get("password")

        if login is None or password is None:
            raise exceptions.AuthenticationFailed("Login or Password not informed")

        user = self.get_queryset().filter(email=login).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Wrong password")

        serializer = self.get_serializer(user)

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        return Response(
            {"access_token": access_token, "refresh_token": refresh_token, "user": serializer.data}, status=status.HTTP_200_OK
        )

    @action(methods=["POST"], detail=False, url_path="refresh", permission_classes=[AllowAny])
    def refresh_token(self, request: HttpRequest):
        refresh_token = request.data.get("refresh_token")
        if refresh_token is None:
            raise exceptions.AuthenticationFailed("Authentication credentials were not provided.")

        try:
            payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Expired refresh token, please login again.")

        user = self.get_queryset().filter(id=payload["user_id"]).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is inactive")

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        return Response({"access_token": access_token, "refresh_token": refresh_token}, status=status.HTTP_200_OK)
