from app.website.models import Website


class About(Website):
    class Meta:
        proxy = True
        verbose_name = "Sobre Mim"
        verbose_name_plural = "Sobre Mim"
