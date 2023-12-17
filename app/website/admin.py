from django.contrib import admin

from .models import Website, About, Header


class HeaderInline(admin.StackedInline):
    model = Header


class AboutInline(admin.StackedInline):
    model = About


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "is_active")
    list_display_links = ("id", "description")
    fieldsets = ((None, {"fields": ("description", "is_active")}),)
    inlines = [HeaderInline, AboutInline,]

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            Website.objects.filter(is_active=True).exclude(id=obj.id).update(
                is_active=False
            )
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        if Website.objects.get_queryset().count() > 2:
            return False
        return True
