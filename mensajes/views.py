from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages as msg
from .models import Mensaje
from .forms import MensajeForm


@login_required
def inbox(request):
    """Bandeja de entrada del usuario logueado."""
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    # Marca como leídos al abrir la bandeja
    mensajes_recibidos.filter(leido=False).update(leido=True)
    return render(request, 'mensajes/inbox.html', {'mensajes': mensajes_recibidos})


@login_required
def enviar_mensaje(request):
    """Enviar un nuevo mensaje a otro usuario."""
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            msg.success(request, '¡Mensaje enviado!')
            return redirect('inbox')
    else:
        # Si viene de un perfil, precarga el destinatario
        destinatario_id = request.GET.get('para')
        form = MensajeForm(initial={'destinatario': destinatario_id} if destinatario_id else {})
    return render(request, 'mensajes/enviar.html', {'form': form})


@login_required
def enviados(request):
    """Mensajes enviados por el usuario."""
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'mensajes/enviados.html', {'mensajes': mensajes_enviados})
