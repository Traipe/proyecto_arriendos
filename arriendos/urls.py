"""from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    UsuarioListView,
    UsuarioDetailView,
    UsuarioCreateView,
    UsuarioUpdateView,
    UsuarioDeleteView,
    HomeView,
    PropiedadListView,
    PropiedadDetailView,
    PropiedadCreateView,
    PropiedadUpdateView,
    PropiedadDeleteView,
    ProfileView,
    RegisterView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='arriendos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='arriendos/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario_detail'),
    path('usuarios/create/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/update/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/delete/', UsuarioDeleteView.as_view(), name='usuario_delete'),
    path('propiedades/', PropiedadListView.as_view(), name='propiedad_list'),
    path('propiedades/<int:pk>/', PropiedadDetailView.as_view(), name='propiedad_detail'),
    path('propiedades/create/', PropiedadCreateView.as_view(), name='propiedad_create'),
    path('propiedades/<int:pk>/update/', PropiedadUpdateView.as_view(), name='propiedad_update'),
    path('propiedades/<int:pk>/delete/', PropiedadDeleteView.as_view(), name='propiedad_delete'),
]
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='arriendos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='arriendos/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.HomeView.as_view(), name='home'),
    path('usuarios/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario_detail'),
    path('usuarios/nuevo/', views.UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/editar/', views.UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuarios/<int:pk>/eliminar/', views.UsuarioDeleteView.as_view(), name='usuario_delete'),
    path('propiedades/', views.PropiedadListView.as_view(), name='propiedad_list'),
    path('propiedades/<int:pk>/', views.PropiedadDetailView.as_view(), name='propiedad_detail'),
    path('propiedades/nueva/', views.PropiedadCreateView.as_view(), name='propiedad_create'),
    path('propiedades/<int:pk>/editar/', views.PropiedadUpdateView.as_view(), name='propiedad_update'),
    path('propiedades/<int:pk>/eliminar/', views.PropiedadDeleteView.as_view(), name='propiedad_delete'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]


