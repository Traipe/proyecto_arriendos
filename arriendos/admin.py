from django.contrib import admin
from .models import Usuario, Propiedad, Region, Comuna, TipoInmueble

admin.site.register(Usuario)
admin.site.register(Propiedad)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(TipoInmueble)
