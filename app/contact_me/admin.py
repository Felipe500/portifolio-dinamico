from django.contrib import admin

from .models import ContactMe


@admin.register(ContactMe)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "subject", "is_answered")
    list_display_links = ("name", "email")
    readonly_fields = ["name", "email", "phone", "subject", "message"]
    fieldsets = (
        (
            None,
            {
             "fields": (
                    "name",
                    "email",
                    "phone",
                    "subject",
                    "message",
                    "is_answered",
                )
            },
        ),
    )
