from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status

from users.serializers import UserSerializer
from users.models import User


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["GET"], detail=False, url_path="profile", permission_classes=[IsAuthenticated])
    def profile(self, request: HttpRequest):
        user = request.user
        serializer = self.get_serializer(user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=False, url_path="create", permission_classes=[AllowAny])
    def create_user(self, request: HttpRequest):
        new_user = request.data

        serializer = self.get_serializer(data=new_user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(type(serializer.data))
        print(serializer.data["password"])
        del serializer.data["password"]

        return Response(serializer.data, status=status.HTTP_201_CREATED)
