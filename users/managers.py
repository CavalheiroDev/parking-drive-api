from django.contrib.auth.models import BaseUserManager
from typing import Dict, Optional


class UserManager(BaseUserManager):
    def __init__(self) -> None:
        super().__init__()

    def create_user(self, email: str, cpf: Optional[str] = None, password: Optional[str] = None, **kwargs: Dict):
        user = self.model(email=email, cpf=cpf, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
