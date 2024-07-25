import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_arriendos.settings')
django.setup()

print("Django está configurado correctamente.")
