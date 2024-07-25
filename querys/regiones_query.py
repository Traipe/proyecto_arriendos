import sys
import os
import django

# directorio del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_arriendos.settings')
django.setup()

from arriendos.models import Propiedad

def listar_inmuebles_por_region(region_nombre):
    inmuebles = Propiedad.objects.filter(comuna__region__nombre=region_nombre).values('nombre', 'descripcion')
    with open(f'inmuebles_{region_nombre}.txt', 'w') as f:
        for inmueble in inmuebles:
            f.write(f"Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}\n")

if __name__ == '__main__':
    listar_inmuebles_por_region('Región de Arica y Parinacota')