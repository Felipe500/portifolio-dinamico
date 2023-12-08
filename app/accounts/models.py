from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.utils.translation import gettext as _

from app.common.models import BaseModel


from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    name = models.CharField(
        max_length=255, verbose_name=_("Nome"), null=True, blank=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        error_messages={"unique": "Usuário com e-mail já existente."},
    )
    phone = models.CharField(
        max_length=255, verbose_name=_("Telefone"), blank=True, null=True
    )
    access_group = models.ForeignKey(
        Group,
        verbose_name=_("group"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="access_group_user",
    )
    is_staff = models.BooleanField(
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
        verbose_name="Acesso ao Dashboard?",
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
        verbose_name="Ativo?",
    )
    ip = models.GenericIPAddressField(
        blank=True, null=True, verbose_name="IP de Registro"
    )
    agent = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Dispositivo"
    )
    last_login = None

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")
