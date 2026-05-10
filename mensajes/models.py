from django.db import models
from django.contrib.auth.models import User


class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recibidos')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return f'De {self.remitente} a {self.destinatario} — {self.fecha:%d/%m/%Y}'
