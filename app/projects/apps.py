from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = "app.projects"
    label = "app_projects"
    verbose_name = "Projetos"

    def ready(self) -> None:
        from . import signals  # noqa: F401