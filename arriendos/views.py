from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Usuario, Propiedad
from django.views.generic import TemplateView

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'user_list.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'user_detail.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'user_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuario_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'user_delete.html'
    success_url = reverse_lazy('usuario_list')

class HomeView(TemplateView):
    template_name = 'arriendos/home.html'

class PropiedadListView(ListView):
    model = Propiedad
    template_name = 'property_list.html'

class PropiedadDetailView(DetailView):
    model = Propiedad
    template_name = 'property_detail.html'

class PropiedadCreateView(CreateView):
    model = Propiedad
    template_name = 'property_form.html'
    fields = '__all__'
    success_url = reverse_lazy('propiedad_list')

class PropiedadUpdateView(UpdateView):
    model = Propiedad
    template_name = 'property_form.html'
    fields = '__all__'
    success_url = reverse_lazy('propiedad_list')

class PropiedadDeleteView(DeleteView):
    model = Propiedad
    template_name = 'property_delete.html'
    success_url = reverse_lazy('propiedad_list')
