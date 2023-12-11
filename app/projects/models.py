from django.contrib.postgres.fields import ArrayField
from django.db import models

from app.common.models import BaseModel
from app.common.fields import ImageField
from app.common.choices import TYPE_PROJECT
from app.common.constants import SET_PLAIN_ICONS, ICONS
from app.common.utils import image_resize, make_thumbnail


class Project(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Nome do projeto", null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name="Descrição", null=True, blank=True)
    cover = ImageField(upload_to='projects/cover/%Y/%m/%d/', verbose_name='Capa', blank=True, null=True)
    thumbnail = ImageField(upload_to="projects/thumbnails/", verbose_name='Miniatura da Capa', blank=True, null=True)
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
    icons = models.JSONField(default=dict, blank=True, null=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self) -> str:
        return f"Projeto | {self.title}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._prev_cover = getattr(self, 'cover', None)

    def save(self, *args, **kwargs):
        if self.cover and self.cover != self._prev_cover:
            make_thumbnail(self, 'cover', 'thumbnail', (350, 350))
            image_resize(self.cover, (1280, 720))
        super().save(*args, **kwargs)

    def update_icons(self):
        print('update_icons')
        html = ""
        for tag in self.tags:
            if tag in list(SET_PLAIN_ICONS.keys()):
                html += ICONS['plain'].format(tag)
            else:
                html += ICONS['original'].format(tag, tag)
        print(html)
        Project.objects.get_queryset().filter(id=self.id).update(icons={'icons': html})
        # print(tag)
