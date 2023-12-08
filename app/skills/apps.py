from django.apps import AppConfig


class SkillsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.skills"
    label = "app_skills"
    verbose_name = "Habilidades"

    def ready(self) -> None:
        from . import signals  # noqa: F401