from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth básico
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # Perfil
    path('perfil/<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('perfil/editar/', views.edit_profile, name='edit_profile'),
    path('perfil/contrasena/', views.change_password, name='change_password'),
]
