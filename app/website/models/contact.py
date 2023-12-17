from django.db import models

from app.common.models import BaseModel

from ..models.website import Website


class Contact(BaseModel):
    email = models.CharField(max_length=255, verbose_name="email", default="email@gmail.com")
    whatsapp = models.CharField(max_length=255, verbose_name="whatsapp", default="86999605077")
    github = models.CharField(max_length=255, verbose_name="Github", default="gitlab.com")
    gitlab = models.CharField(max_length=255, verbose_name="Gitlab", default="github.com")
    stackoverflow = models.CharField(max_length=255, verbose_name="Stackoverflow", default="stackoverflow.com")
    linkedin = models.CharField(max_length=255, verbose_name="Linkedin", default="linkedin.com")

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
        }
        Website.objects.filter(id=self.website.id).update(contact=data)
