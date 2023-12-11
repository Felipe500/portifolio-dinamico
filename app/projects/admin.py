from django.contrib import admin

from .models import Project
from .forms import ProjectForm


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "website")
    list_display_links = ("id", "title")
    form = ProjectForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "website",
                    "title",
                    "description",
                    "cover",
                    "thumbnail",
                    "type",
                    "demo_link",
                    "source_link",
                    "tags",
                )
            },
        ),
    )
