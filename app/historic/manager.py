from django.db.models.query import QuerySet

from app.common.models import SoftDeletionManager


class HistoricManager(SoftDeletionManager):
    def __init__(self, type_historic: str) -> None:
        self.type_historic = type_historic
        super().__init__()

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(type=self.type_historic)
