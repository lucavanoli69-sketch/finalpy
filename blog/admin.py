from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha')
    list_filter = ('fecha', 'autor')
    search_fields = ('titulo', 'subtitulo', 'contenido')
    date_hierarchy = 'fecha'
