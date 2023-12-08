from django.contrib import admin

from .models import Website
from app.skills.models import HardSkill, CardSkill


class SkillInline(admin.TabularInline):
    model = HardSkill
    extra = 1


class CardHardSkillInline(admin.StackedInline):
    model = CardSkill
    extra = 1


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "is_active")
    list_display_links = ("id", "description")
    fieldsets = ((None, {"fields": ("description", "is_active")}),)
    inlines = [SkillInline, CardHardSkillInline]

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            Website.objects.filter(is_active=True).exclude(id=obj.id).update(
                is_active=False
            )
        super().save_model(request, obj, form, change)
