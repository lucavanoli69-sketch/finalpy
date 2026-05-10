from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignupForm, ProfileForm, CustomPasswordChangeForm
from .models import Profile


def signup(request):
    """Registro de nuevo usuario."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


# CBV: Vista del perfil público de un usuario
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'profile_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()
        return context


@login_required
def edit_profile(request):
    """Editar perfil del usuario logueado."""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def change_password(request):
    """Cambio de contraseña."""
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Mantiene la sesión activa tras el cambio
            update_session_auth_hash(request, user)
            messages.success(request, '¡Contraseña cambiada con éxito!')
            return redirect('profile', username=request.user.username)
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
