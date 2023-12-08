from django.contrib import admin

from .models import Project
from app.skills.models import HardSkill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "website")
    list_display_links = ("id", "title")
