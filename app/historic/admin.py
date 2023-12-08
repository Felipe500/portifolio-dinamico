from django.contrib import admin
from .models import HistoricAcademic, HistoricProfessional


@admin.register(HistoricAcademic)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "institution_company", "website")
    list_display_links = ("id", "name", "institution_company")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "website",
                    "name",
                    "institution_company",
                    "description",
                    "start_date",
                    "end_date",
                    "address",
                )
            },
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields["name"].label = "Curso"
        form.base_fields["institution_company"].label = "Instituição Acadêmica"
        return form

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.type = "academic"
        super().save_model(request, obj, form, change)


@admin.register(HistoricProfessional)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "institution_company", "website")
    list_display_links = ("id", "name", "institution_company")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "website",
                    "name",
                    "institution_company",
                    "description",
                    "start_date",
                    "end_date",
                    "address",
                )
            },
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields["name"].label = "Cargo"
        form.base_fields["institution_company"].label = "Empresa"
        return form

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        obj.type = "professional"
        super().save_model(request, obj, form, change)
