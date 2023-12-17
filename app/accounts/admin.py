from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from app.accounts.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "id",
        "name",
        "email",
    )
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_superuser", "is_staff", "groups")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "password1", "password2"),
            },
        ),
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
