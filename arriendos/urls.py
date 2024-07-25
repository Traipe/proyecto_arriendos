"""
URL configuration for proyecto_arriendos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
------

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.urls import path
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
    PropiedadDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
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
