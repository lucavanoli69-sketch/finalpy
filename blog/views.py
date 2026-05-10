from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post
from .forms import PostForm


# CBV: Lista de todos los posts (Home)
class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 6


# CBV: Detalle de un post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# CBV: Lista de páginas (igual que home pero diferente template)
class PagesView(ListView):
    model = Post
    template_name = 'blog/pages.html'
    context_object_name = 'posts'


# CBV: Crear post — requiere login (Mixin)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Asigna el autor automáticamente al usuario logueado
        form.instance.autor = self.request.user
        messages.success(self.request, '¡Post publicado con éxito!')
        return super().form_valid(form)


# CBV: Editar post — requiere login
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, '¡Post actualizado correctamente!')
        return super().form_valid(form)


# Función: Borrar post — usa decorador login_required
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post eliminado.')
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


# Vista estática About
def about(request):
    return render(request, 'blog/about.html')
