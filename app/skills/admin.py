from django.contrib import admin

from .models import SoftSkill, HardSkill, CardSkill


class SkillInline(admin.StackedInline):
    model = HardSkill
    extra = 1
    fields = ['name', 'time_experience', 'order']


@admin.register(CardSkill)
class CardHardSkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "order", "website")
    list_display_links = ("id", "name",)
    inlines = [SkillInline]
