from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Historic, HistoricAcademic, HistoricProfessional
from app.common.constants import default_website


@receiver(post_save, sender=HistoricAcademic)
def create_new_historic_academic(sender, instance, created, **kwargs):
    Historic.update_historic(instance)


@receiver(post_save, sender=HistoricProfessional)
def create_new_historic_professional(sender, instance, created, **kwargs):
    Historic.update_historic(instance)
