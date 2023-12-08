from django.db.models.query import QuerySet

from app.common.models import SoftDeletionManager


class SkillManager(SoftDeletionManager):
    def __init__(self, type_skill: str) -> None:
        self.type_skill = type_skill
        super().__init__()

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(type=self.type_skill)
