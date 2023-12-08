from django.apps import AppConfig


class HistoricConfig(AppConfig):
    name = "app.historic"
    label = "app_historic"
    verbose_name = "Historico"

    def ready(self) -> None:
        from . import signals  # noqa: F401
