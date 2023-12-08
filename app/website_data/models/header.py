from app.website.models import Website


class Header(Website):
    class Meta:
        proxy = True
        verbose_name = "Cabeçalho da página"
        verbose_name_plural = "Cabeçalhos das páginas"
