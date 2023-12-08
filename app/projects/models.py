from django.contrib.postgres.fields import ArrayField
from django.db import models

from app.common.models import BaseModel
from app.common.fields import ImageField
from app.common.choices import TYPE_PROJECT
from app.common.utils import image_resize, make_thumbnail


class Project(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Nome do projeto", null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name="Descrição", null=True, blank=True)
    cover = ImageField(blank=True, null=True, upload_to='projects/cover/%Y/%m/%d/')
    thumbnail = ImageField(upload_to="projects/thumbnails/", verbose_name='Miniatura foto', blank=True, null=True)
    type = models.CharField(choices=TYPE_PROJECT, verbose_name="Tipo de Projeto", default=TYPE_PROJECT.full_stack)
    demo_link = models.CharField(
        verbose_name="Link do projeto em produção:",
        max_length=2000,
        null=True,
        blank=True,
    )
    source_link = models.CharField(
        verbose_name="Link do repositório do projeto:",
        max_length=2000,
        null=True,
        blank=True,
    )
    website = models.ForeignKey(
        "app_website.Website",
        verbose_name="Website",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    tags = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        null=True,
        verbose_name="Tags",
        help_text="Separado por virgula ,",
    )

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self) -> str:
        return f"Projeto | {self.title}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self._prev_cover = self.cover
        except Exception:
            self._prev_cover = 0

    def save(self, *args, **kwargs):
        if self.cover and self.cover != self._prev_cover:
            make_thumbnail(self, 'photo', 'thumbnail', (250, 250))
            image_resize(self.cover, (1280, 720))
        super().save(*args, **kwargs)
