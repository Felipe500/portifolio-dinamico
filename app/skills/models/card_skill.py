from django.db import models

from app.common.models import BaseModel
from app.website.models import Website


class CardSkill(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Nome', help_text='FRONT-END, BACK-END, MOBILE...')
    website = models.ForeignKey(
        "app_website.Website",
        verbose_name="Website",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(default=1, verbose_name='Ordenação', help_text='Número da ordem de exibição.')

    class Meta:
        verbose_name = 'Cartão de Habilidades'
        verbose_name_plural = 'Cartões de Habilidades'
        ordering = ['order']

    def __str__(self) -> str:
        return f"{self.name}"

    def update_skills_card_website(self):
        skills_card = [obj for obj in CardSkill.objects.get_queryset().values('id', 'name')]
        for skill_card in skills_card:
            skill_card['id'] = str(skill_card['id'])
        print(skills_card)
        Website.objects.filter(id=self.website.id).update(skills_card=skills_card)
