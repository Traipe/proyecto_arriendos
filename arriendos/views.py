from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario, Propiedad
import json
from django.conf import settings
import os


# Vista para listar usuarios
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'arriendos/user_list.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'arriendos/user_detail.html'

# Vista para crear un usuario
class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'arriendos/user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

# Vista para actualizar un usuario
class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'arriendos/user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

# Vista para eliminar un usuario
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'arriendos/user_delete.html'
    success_url = reverse_lazy('usuario_list')

# Vista para la página de inicio
class HomeView(TemplateView):
    template_name = 'arriendos/home.html'

# Función para cargar datos desde archivos JSON
def cargar_datos(archivo):
    ruta_archivo = os.path.join(settings.BASE_DIR, 'arriendos', 'fixtures', archivo)
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        return json.load(file)

# Vista para la página principal
def home(request):
    inmuebles = cargar_datos('inmuebles.json')
    comunas = cargar_datos('comunas.json')
    regiones = cargar_datos('regiones.json')
    tipos_inmuebles = cargar_datos('tipos_inmuebles.json')
    usuarios = cargar_datos('usuarios.json')
    comuna_seleccionada = request.GET.get('comuna')
    region_seleccionada = request.GET.get('region')

    if comuna_seleccionada:
        inmuebles = [inmueble for inmueble in inmuebles if inmueble['comuna'] == comuna_seleccionada]
    if region_seleccionada:
        inmuebles = [inmueble for inmueble in inmuebles if inmueble['region'] == region_seleccionada]
    
    return render(request, 'home.html', {
        'inmuebles': inmuebles,
        'comunas': comunas,
        'regiones': regiones,
        'tipos_inmuebles': tipos_inmuebles,
        'usuarios': usuarios,
        'comuna_seleccionada': comuna_seleccionada,
        'region_seleccionada': region_seleccionada
    })

# Vista para listar propiedades
class PropiedadListView(ListView):
    model = Propiedad
    template_name = 'arriendos/property_list.html'

# Vista para el detalle de una propiedad
class PropiedadDetailView(DetailView):
    model = Propiedad
    template_name = 'arriendos/property_detail.html'

# Vista para crear una propiedad
class PropiedadCreateView(CreateView):
    model = Propiedad
    template_name = 'arriendos/property_form.html'
    fields = '__all__'
    success_url = reverse_lazy('propiedad_list')

# Vista para actualizar una propiedad
class PropiedadUpdateView(UpdateView):
    model = Propiedad
    template_name = 'arriendos/property_form.html'
    fields = '__all__'
    success_url = reverse_lazy('propiedad_list')

# Vista para eliminar una propiedad
class PropiedadDeleteView(DeleteView):
    model = Propiedad
    template_name = 'arriendos/property_delete.html'
    success_url = reverse_lazy('propiedad_list')

# Vista de perfil para usuarios autenticados
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'arriendos/profile.html'

# Vista para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirige a la vista de éxito
    else:
        form = UserCreationForm()
    return render(request, 'arriendos/register.html', {'form': form})

# Vista de éxito después del registro
def success(request):
    return render(request, 'arriendos/success.html')

# Vista personalizada de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/welcome')
        else:
            error_message = 'Los caracteres son incorrectos'
            print("Autenticación fallida")
            return render(request, 'arriendos/login.html', {'error_message': error_message})
    else:
        return render(request, 'arriendos/login.html')

# Vista personalizada de cierre de sesión
class CustomLogoutView(auth_views.LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# Vista para el detalle de una tarjeta específica
def detalle_card(request, card_id):
    inmuebles = cargar_datos('inmuebles.json')
    card = next((item for item in inmuebles if item['pk'] == card_id), None)
    if card is None:
        return render(request, '404.html', status=404)
    return render(request, 'detalle.html', {'inmueble': inmueble})

# Vista para editar el perfil del usuario
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Los cambios han sido guardados con éxito!')
            return redirect('profile')  
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'arriendos/edit_profile.html', {'form': form})

# Vista de bienvenida después del inicio de sesión
def welcome(request):
    return render(request, 'arriendos/welcome.html')
