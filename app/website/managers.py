from typing import List

from app.common.models import SoftDeletionManager


class WebsiteManager(SoftDeletionManager):
    def get_queryset(self) -> List:
        return super().get_queryset().filter(using="using")
