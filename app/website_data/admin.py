from django.contrib import admin

from .models import About, Header, SocialMedia


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "view_header_wellcome_title",
        "header_profession",
    )
    list_display_links = (
        "id",
        "description",
        "view_header_wellcome_title",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "header_wellcome_title",
                    "header_profession",
                    "header_description",
                    "header_photo",
                )
            },
        ),
    )

    def view_header_wellcome_title(self, obj):
        return f"{obj.header_wellcome_title if obj.header_wellcome_title else 'Sem Mensagem'}"

    view_header_wellcome_title.short_description = "Mensagem de boas-vindas"

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(About)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "view_title", "email")
    list_display_links = (
        "id",
        "description",
        "view_title",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "content",
                    "email",
                    "phone",
                    "photo",
                    "birth_date",
                    "is_freelance",
                    "nationality",
                    "address",
                    "languages",
                )
            },
        ),
    )

    def view_title(self, obj):
        return f"{obj.title if obj.title else 'sem titulo'}"

    view_title.short_description = "Titulo"

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "view_email", "github", "linkedin")
    list_display_links = (
        "id",
        "description",
        "view_email",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "github",
                    "gitlab",
                    "stackoverflow",
                    "linkedin",
                    "facebook",
                )
            },
        ),
    )

    def view_email(self, obj):
        return f"{obj.email if obj.email else 'Sem Email'}"

    view_email.short_description = "Email"

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
