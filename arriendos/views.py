from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Usuario, Propiedad

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'arriendos/user_list.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'arriendos/user_detail.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'arriendos/user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'arriendos/user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'arriendos/user_delete.html'
    success_url = reverse_lazy('usuario_list')

class HomeView(TemplateView):
    template_name = 'arriendos/home.html'

class PropiedadListView(ListView):
    model = Propiedad
    template_name = 'arriendos/property_list.html'

class PropiedadDetailView(DetailView):
    model = Propiedad
    template_name = 'arriendos/property_detail.html'

class PropiedadCreateView(CreateView):
    model = Propiedad
    template_name = 'arriendos/property_form.html'
    fields = '__all__'
    success_url = reverse_lazy('propiedad_list')

class PropiedadUpdateView(UpdateView):
    model = Propiedad
    template_name = 'arriendos/property_form.html'
    fields = '__all__'
    success_url = reverse_lazy('propiedad_list')

class PropiedadDeleteView(DeleteView):
    model = Propiedad
    template_name = 'arriendos/property_delete.html'
    success_url = reverse_lazy('propiedad_list')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'arriendos/profile.html'

class RegisterView(TemplateView):
    template_name = 'arriendos/register.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'arriendos/register.html', {'form': form})


class PasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'