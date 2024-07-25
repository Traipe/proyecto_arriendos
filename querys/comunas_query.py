import os
import sys
import django


#directorio raiz agregado a PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#config django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_arriendos.settings')
django.setup()

from django.core.management.base import BaseCommand
from arriendos.models import Propiedad

def listar_inmuebles_por_comuna(comuna_nombre):
    inmuebles = Propiedad.objects.filter(comuna__nombre=comuna_nombre).values('nombre', 'descripcion')
    with open('inmueble_comunas.txt', 'w', encoding='utf-8') as f:
        for inmueble in inmuebles:
            f.write(f"Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}\n")
            print(f"Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}")

if __name__ == "__main__":
    listar_inmuebles_por_comuna('Arica')