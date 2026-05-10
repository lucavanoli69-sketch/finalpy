from django import forms
from django.contrib.auth.models import User
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select bg-dark text-light border-secondary'}),
        label='Para',
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'rows': 5,
                'placeholder': 'Escribe tu mensaje...',
            }),
        }
        labels = {
            'contenido': 'Mensaje',
        }
