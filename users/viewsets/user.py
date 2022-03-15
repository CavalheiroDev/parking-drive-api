from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status

from users.serializers import UserSerializer
from users.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes_by_action = {"create": [AllowAny], "list": [AllowAny]}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    @action(methods=["GET"], detail=False, url_path="profile", permission_classes=[IsAuthenticated])
    def profile(self, request: HttpRequest):
        user = request.user
        serializer = self.get_serializer(user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)
