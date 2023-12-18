import locale

from django.utils import timezone
from django.db import models
from django.forms.models import model_to_dict

from app.common.models import BaseModel
from app.common.choices import TYPE_HISTORIC
from app.website.models import Website

from .manager import HistoricManager


class Historic(BaseModel):
    name = models.CharField(
        max_length=255, verbose_name="Nome do Curso ou Cargo", null=True, blank=True
    )
    institution_company = models.CharField(
        max_length=255, verbose_name="Instituição ou Empresa", null=True, blank=True
    )
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)
    type = models.CharField(
        choices=TYPE_HISTORIC, verbose_name="Tipo de ", default=TYPE_HISTORIC.academic
    )
    start_date = models.DateField(verbose_name="Data de Início", blank=True, null=True)
    end_date = models.DateField(verbose_name="Data de Término", blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    website = models.ForeignKey(
        "app_website.Website",
        verbose_name="Website",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="website",
    )

    class Meta:
        verbose_name = "Historico"
        verbose_name_plural = "Historicos"
        ordering = ['-end_date']

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def update_historic(self):
        data_historic = {}
        list_historic = []
        locale.setlocale(locale.LC_ALL, locale.getlocale())
        queryset_historic = Historic.objects.get_queryset().filter(website=self.website)

        for instance in queryset_historic:
            data_json = model_to_dict(instance)
            data_json["start_date"] = instance.start_date.strftime("%B %Y").title()
            data_json["end_date"] = timezone.datetime.strftime(
                instance.end_date, "%B %Y"
            ).title()
            list_historic.append(data_json)

        data_historic['academic'] = [d for d in list_historic if d["type"] in ["academic"]]
        data_historic['professional'] = [d for d in list_historic if d["type"] in ["professional"]]

        Website.objects.filter(id=self.website.id).update(historic=data_historic)


class HistoricAcademic(Historic):
    objects = HistoricManager(type_historic=TYPE_HISTORIC.academic)

    class Meta:
        proxy = True
        verbose_name = "Historico Academico"
        verbose_name_plural = "Historicos Academicos"

    def __str__(self) -> str:
        return f"{self.name} | {self.institution_company}"


class HistoricProfessional(Historic):
    objects = HistoricManager(type_historic=TYPE_HISTORIC.professional)

    class Meta:
        proxy = True
        verbose_name = "Historico Profissional"
        verbose_name_plural = "Historicos Profissional"

    def __str__(self) -> str:
        return f"{self.name} | {self.institution_company}"
