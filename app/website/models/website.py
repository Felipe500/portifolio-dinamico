from django.db import models

from app.common.models import BaseModel


class Website(BaseModel):
    description = models.CharField(max_length=255, verbose_name="Descrição website", null=True, blank=True)
    header = models.JSONField(default=dict, verbose_name="Cabeçalho da página")
    about = models.JSONField(default=dict, verbose_name="Cabeçalho da página")
    historic = models.JSONField(default=list, verbose_name="Historicos acadêmicos e profissionais")
    skills = models.JSONField(default=list, verbose_name="Habilidades")
    skills_card = models.JSONField(default=list, verbose_name="Card de Habilidades")
    github = models.CharField(max_length=255, verbose_name="Github", null=True, blank=True)
    gitlab = models.CharField(max_length=255, verbose_name="Gitlab", null=True, blank=True)
    stackoverflow = models.CharField(max_length=255, verbose_name="Stackoverflow", null=True, blank=True)
    linkedin = models.CharField(max_length=255, verbose_name="Linkedin", null=True, blank=True)
    facebook = models.CharField(max_length=255, verbose_name="Facebook", null=True, blank=True)

    is_active = models.BooleanField(default=False, verbose_name="Ativo?")

    class Meta:
        verbose_name = "website"
        verbose_name_plural = "websites"

    def __str__(self):
        return f"website | {self.description}"
