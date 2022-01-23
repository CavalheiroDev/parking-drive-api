from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "cpf",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
        ]
