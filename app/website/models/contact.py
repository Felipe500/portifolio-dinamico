from django.db import models

from app.common.models import BaseModel

from ..models.website import Website


class Contact(BaseModel):
    email = models.CharField(max_length=255, verbose_name="email", null=True, blank=True)
    whatsapp = models.CharField(max_length=255, verbose_name="whatsapp", null=True, blank=True)
    github = models.CharField(max_length=255, verbose_name="Github", null=True, blank=True)
    gitlab = models.CharField(max_length=255, verbose_name="Gitlab", null=True, blank=True)
    stackoverflow = models.CharField(max_length=255, verbose_name="Stackoverflow", null=True, blank=True)
    linkedin = models.CharField(max_length=255, verbose_name="Linkedin", null=True, blank=True)
    facebook = models.CharField(max_length=255, verbose_name="Facebook", null=True, blank=True)

    website = models.OneToOneField(
        "app_website.Website",
        verbose_name="Website",
        on_delete=models.CASCADE,
        related_name='app_website_contact',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Dados para contato"
        verbose_name_plural = "Dados para contato"

    def __str__(self):
        return f"Dados contato | website: {self.website.description}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_contact_website()

    def update_contact_website(self):
        data = {
            'email': self.email,
            'whatsapp': self.whatsapp,
            'github': self.github,
            'gitlab': self.gitlab,
            'stackoverflow': self.stackoverflow,
            'linkedin': self.linkedin,
            'facebook': self.facebook,
        }
        Website.objects.filter(id=self.website.id).update(contact=data)
