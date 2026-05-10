from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    contenido = RichTextUploadingField()  # Editor enriquecido con CKEditor
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
