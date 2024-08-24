from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    UsuarioListView, UsuarioDetailView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView,
    HomeView, PropiedadListView, PropiedadDetailView, PropiedadCreateView, PropiedadUpdateView,
    PropiedadDeleteView, ProfileView, edit_profile
)

urlpatterns = [
    path('', views.home, name='home'),
    path('detalle/<int:card_id>/', views.detalle_card, name='detalle_card'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'), 
    path('login/', auth_views.LoginView.as_view(template_name='arriendos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='arriendos/logout.html'), name='logout'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario_detail'),
    path('usuarios/nuevo/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
    path('propiedades/', PropiedadListView.as_view(), name='propiedad_list'),
    path('propiedades/<int:pk>/', PropiedadDetailView.as_view(), name='propiedad_detail'),
    path('propiedades/nueva/', PropiedadCreateView.as_view(), name='propiedad_create'),
    path('propiedades/<int:pk>/editar/', PropiedadUpdateView.as_view(), name='propiedad_update'),
    path('propiedades/<int:pk>/eliminar/', PropiedadDeleteView.as_view(), name='propiedad_delete'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='arriendos/password_reset_form.html'), name='password_reset'),
    path('welcome/', views.welcome, name='welcome'),
]
