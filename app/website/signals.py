from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Website, About, Header
from app.common.constants import default_website


@receiver(post_save, sender=Website)
def create_website(sender, instance, created, **kwargs):
    if created:
        if not About.objects.get_queryset().filter(website_id=instance.id).exists():
            About.objects.create(website=instance)

        if not Header.objects.get_queryset().filter(website_id=instance.id).exists():
            Header.objects.create(website=instance)
