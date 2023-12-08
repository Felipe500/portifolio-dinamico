from django.db import models

from app.common.models import BaseModel


class SoftSkill(BaseModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, verbose_name="Descrição", null=True, blank=True)
    website = models.ForeignKey(
        "app_website.Website",
        verbose_name="Website",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(default=1, verbose_name='Ordenação', help_text='Número da ordem de exibição.')

    class Meta:
        verbose_name = "Soft Skill"
        verbose_name_plural = "Soft Skills"

    def __str__(self) -> str:
        return f"SoftSkill | {self.name}"
