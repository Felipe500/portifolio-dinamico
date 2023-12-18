from django.db import models

from app.common.fields import ImageField
from app.common.models import BaseModel
from app.common.utils import image_resize

from ..models.website import Website


class Header(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Mensagem de boas-vindas", default="Mensagem de boas-vindas")
    profession = models.CharField(max_length=255, verbose_name="Profissão", default="Profissão")
    subtitle = models.TextField(max_length=255, verbose_name="Subtítulo", default="Descubra mais sobre mim...")
    photo = ImageField(
        verbose_name="Foto do cabeçalho",
        upload_to="website/header/%Y/%m/%d/",
        blank=True,
        null=True,
    )
    website = models.OneToOneField(
        "app_website.Website",
        verbose_name="Website",
        on_delete=models.CASCADE,
        related_name='app_website_header',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Cabeçalho Website"
        verbose_name_plural = "Cabeçalho Website"

    def __str__(self):
        return f"Cabeçalho | website: {self.website.description}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._prev_photo = getattr(self, 'photo', None)

    def save(self, *args, **kwargs):
        if self.photo and self.photo != self._prev_photo:
            image_resize(self.photo, (1280, 720))
        super().save(*args, **kwargs)
        self.update_header_website()

    def update_header_website(self):
        data = {
            'title': self.title,
            'profession': self.profession,
            'subtitle': self.subtitle,
            'photo': getattr(self.photo, 'url') if self.photo else ''
        }
        Website.objects.filter(id=self.website.id).update(header=data)
