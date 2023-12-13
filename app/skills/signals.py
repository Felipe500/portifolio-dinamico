from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import HardSkill, CardSkill


@receiver(post_save, sender=HardSkill)
def update_skills_hard_website(sender, instance, created, **kwargs):
    HardSkill.update_skills_website(instance)


@receiver(post_save, sender=CardSkill)
def update_skills_card_website(sender, instance, created, **kwargs):
    CardSkill.update_skills_card_website(instance)
