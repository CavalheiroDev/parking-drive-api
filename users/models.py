from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Login"), max_length=255, unique=True)
    username = models.CharField(
        _("Username"), max_length=50, unique=True, blank=True, null=True
    )
    cpf = models.CharField(_("CPF"), max_length=11, unique=True, blank=True, null=True)
    first_name = models.CharField(_("Nome"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Sobrenome"), max_length=50, blank=True, null=True)
    is_staff = models.BooleanField(
        _("Acesso ao Painel Administrativo"),
        default=False,
        help_text=_("Permite que o usuário tenha acesso ao Painel Administrativo."),
    )
    is_active = models.BooleanField(
        _("Usuário ativo"),
        default=True,
        help_text=_("Identifica se o usuário está ativo no sistema."),
    )
    is_superuser = models.BooleanField(
        _("Super usuario"),
        default=True,
        help_text=_("Identifica se é um super usuário"),
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return f"{self.id} {self.email}"

    class Meta:
        verbose_name = _("Usuário")
        ordering = ("first_name", "last_name")
