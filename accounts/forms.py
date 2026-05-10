from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile


class SignupForm(UserCreationForm):
    """Formulario de registro con email obligatorio."""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control bg-dark text-light border-secondary',
            'placeholder': 'tu@email.com',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica estilos a todos los campos
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control bg-dark text-light border-secondary')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    """Formulario para editar el perfil de usuario."""
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'rows': 4,
                'placeholder': 'Cuéntanos algo sobre vos...',
            }),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    """Cambio de contraseña con estilos personalizados."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control bg-dark text-light border-secondary'
