from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Título del post...',
            }),
            'subtitulo': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Subtítulo...',
            }),
        }
        labels = {
            'titulo': 'Título',
            'subtitulo': 'Subtítulo',
            'contenido': 'Contenido',
            'imagen': 'Imagen destacada',
        }
