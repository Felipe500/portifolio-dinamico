from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project


@receiver(post_save, sender=Project)
def gerator_icons(sender, instance, created, **kwargs):
    instance.update_icons()
