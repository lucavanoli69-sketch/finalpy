from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.PagesView.as_view(), name='pages'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/nuevo/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/borrar/', views.post_delete, name='post_delete'),
]
