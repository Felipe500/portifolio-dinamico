from django.db import models

from app.common.models import BaseModel


class ContactMe(BaseModel):
    name = models.CharField(verbose_name='Nome', max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=16)
    subject = models.CharField(max_length=175)
    message = models.TextField(verbose_name='Mensagem', blank=True, null=True)
    is_answered = models.BooleanField(default=False, verbose_name='Mensagem Respondida?')

    class Meta:
        verbose_name = 'Contato | Mensagem'
        verbose_name_plural = 'Contatos | Mensagens'
        ordering = ['-created_at', '-updated_at']

    def __str__(self):
        return f"{self.name}"
