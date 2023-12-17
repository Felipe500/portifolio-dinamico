import datetime
from dateutil.relativedelta import relativedelta

from django.contrib.postgres.fields import ArrayField
from django.db import models

from app.common.fields import ImageField
from app.common.models import BaseModel

from ..models.website import Website


class About(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Titulo - Sobre Mim", default="Sobre Mim")
    content = models.TextField(verbose_name="Minha historia", default="Minha história.")
    photo = ImageField(verbose_name="Foto", upload_to="website/perfil/%Y/%m/%d/", blank=True, null=True)
    name = models.CharField(max_length=255, default="Luiz Santana")
    email = models.EmailField(max_length=255, default="email@email.com")
    phone = models.CharField(max_length=16, verbose_name="Telefone", default="879956080")
    birth_date = models.DateField(default=datetime.date.today, verbose_name="Data de Nascimento")
    is_freelance = models.BooleanField(default=False)
    nationality = models.CharField(max_length=80, blank=True, null=True, default="Brasileira")
    address = models.CharField(max_length=80, blank=True, null=True)
    languages = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        null=True,
        verbose_name="linguagem Faladas",
        help_text="Separado por virgula ,",
    )
    website = models.OneToOneField(
        "app_website.Website",
        verbose_name="Website",
        on_delete=models.CASCADE,
        related_name='app_website_about',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Sobre Website"
        verbose_name_plural = "Sobre Website"

    def __str__(self):
        return f"Sobre | website: {self.website.description}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_about_website()

    def update_about_website(self):
        data = {
            'title': self.title or '',
            'content': self.content or '',
            'name': self.name or '',
            'email': self.email or '',
            'phone': self.phone or '',
            'birth_date': self.birth_date.strftime('%d-%m-%Y') or '',
            'years_life':  relativedelta(datetime.date.today(),  self.birth_date).years,
            'is_freelance': self.is_freelance or '',
            'nationality': self.nationality or '',
            'languages': self.languages or '',
            'photo': getattr(self.photo, 'url') if self.photo else ''
        }
        Website.objects.filter(id=self.website.id).update(about=data)
