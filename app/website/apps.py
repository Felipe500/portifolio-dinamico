from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = "app.website"
    label = "app_website"
    verbose_name = "Meu website"

    def ready(self) -> None:
        from . import signals  # noqa: F401
