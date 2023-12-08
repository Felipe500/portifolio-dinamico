from app.website.models import Website


class SocialMedia(Website):
    class Meta:
        proxy = True
        verbose_name = "Midia Social"
        verbose_name_plural = "Midias Sociais"
