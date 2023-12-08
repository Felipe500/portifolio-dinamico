from django.db import models

from app.common.choices import TYPE_HARD_SKILL, TIME_EXPERIENCE_SKILL
from app.common.utils import generator_stars
from app.common.models import BaseModel

from app.website.models import Website

from .card_skill import CardSkill


class HardSkill(BaseModel):
    name = models.CharField(max_length=200)
    type = models.CharField(choices=TYPE_HARD_SKILL, verbose_name="Tipo Skill", default=TYPE_HARD_SKILL.back_end)
    website = models.ForeignKey(
        "app_website.Website",
        verbose_name="Website",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    time_experience = models.CharField(
        choices=TIME_EXPERIENCE_SKILL,
        verbose_name="Tempo de experiência",
        default=TIME_EXPERIENCE_SKILL._0_year_0_month
    )
    card = models.ForeignKey(
        "CardSkill",
        verbose_name="Card Skill",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(default=1, verbose_name='Ordenação', help_text='Número da ordem de exibição.')

    class Meta:
        verbose_name = "Hard Skill"
        verbose_name_plural = "Hard Skills"
        ordering = ['order', 'type']

    def __str__(self) -> str:
        return f"HardSkill | {self.name}"

    def save(self, *args, **kwargs):
        if self.card:
            self.website = self.card.website
        super().save(*args, **kwargs)

    def update_skills_website(self):
        list_skill = []
        queryset_skill = HardSkill.objects.get_queryset()

        for instance in queryset_skill:
            list_skill.append({
                "id": instance.id,
                "name": instance.name,
                "card_id": instance.card.id,
                "time_experience": generator_stars(instance.time_experience),
            })

        card_ids = CardSkill.objects.get_queryset().values_list('id', flat=True)
        print(card_ids)

        card_skill_ = {key: None for key in card_ids}

        for card_skill in card_ids:
            print('card  ', card_skill)
            card_skill_[int(card_skill)] = [d for d in list_skill if d["card_id"] in [card_skill]]

        Website.objects.filter(id=self.website.id).update(skills=card_skill_)
