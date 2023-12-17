from django.db import models

from app.common.models import BaseModel


class Website(BaseModel):
    description = models.CharField(max_length=255, verbose_name="Descrição website", null=True, blank=True)
    header = models.JSONField(default=dict, verbose_name="Cabeçalho da página")
    about = models.JSONField(default=dict, verbose_name="Cabeçalho da página")
    historic = models.JSONField(default=list, verbose_name="Historicos acadêmicos e profissionais")
    skills = models.JSONField(default=list, verbose_name="Habilidades")
    skills_card = models.JSONField(default=list, verbose_name="Card de Habilidades")
    contact = models.JSONField(default=dict, verbose_name="Dados para contato")

    is_active = models.BooleanField(default=False, verbose_name="Ativo?")

    class Meta:
        verbose_name = "website"
        verbose_name_plural = "websites"

    def __str__(self):
        return f"website | {self.description}"
