import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models

from app.common.fields import ImageField
from app.common.models import BaseModel


class Website(BaseModel):
    description = models.CharField(
        max_length=255, verbose_name="Descrição website", null=True, blank=True
    )

    header_wellcome_title = models.CharField(
        max_length=255,
        verbose_name="Mensagem de boas-vindas",
        default="Mensagem de boas-vindas",
    )
    header_profession = models.CharField(
        max_length=255, verbose_name="Profissão", default="Profissão"
    )
    header_description = models.TextField(
        max_length=255, verbose_name="Descrição", default="Descrição"
    )
    header_photo = ImageField(
        verbose_name="Foto do cabeçalho",
        upload_to="website/header/%Y/%m/%d/",
        blank=True,
        null=True,
    )

    title = models.CharField(max_length=255, verbose_name="Titulo - Sobre Mim", default="Sobre Mim")
    content = models.TextField(verbose_name="Minha historia", default="Minha história.")
    photo = ImageField(verbose_name="Foto", upload_to="website/perfil/%Y/%m/%d/", blank=True, null=True)
    name = models.CharField(max_length=255, default="Luiz Santana")
    email = models.EmailField(max_length=255, default="email@email.com")
    phone = models.CharField(max_length=16, verbose_name="Telefone", default="879956080")
    birth_date = models.DateField(default=datetime.date.today(), verbose_name="Data de Nascimento")
    is_freelance = models.BooleanField(default=False)
    nationality = models.CharField(max_length=80, blank=True, null=True, default="Brasileira")
    address = models.CharField(max_length=80, blank=True, null=True)
    languages = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        null=True,
        verbose_name="linguagem Faladas",
        help_text="Separado por virgula ,",
    )

    historic = models.JSONField(
        default=list,
        verbose_name="Historicos acadêmicos e profissionais",
    )
    skills = models.JSONField(
        default=list,
        verbose_name="Habilidades",
    )
    skills_card = models.JSONField(
        default=list,
        verbose_name="Card de Habilidades",
    )
    github = models.CharField(
        max_length=255, verbose_name="https://github.com/", null=True, blank=True
    )
    gitlab = models.CharField(
        max_length=255, verbose_name="https://gitlab.com/", null=True, blank=True
    )
    stackoverflow = models.CharField(
        max_length=255, verbose_name="https://stackoverflow.com/", null=True, blank=True
    )
    linkedin = models.CharField(
        max_length=255, verbose_name="https://linkedin.com/", null=True, blank=True
    )
    facebook = models.CharField(
        max_length=255, verbose_name="https://facebook.com/", null=True, blank=True
    )

    is_active = models.BooleanField(default=False, verbose_name="Ativo?")

    class Meta:
        verbose_name = "website"
        verbose_name_plural = "websites"

    def __str__(self):
        return f"website | {self.description}"
