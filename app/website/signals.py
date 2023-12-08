from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Website
from app.common.constants import default_website


@receiver(post_save, sender=Website)
def create_website(sender, instance, created, **kwargs):
    if created:
        print(dir(instance))
