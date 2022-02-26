from django.contrib import admin
from .models import Service

# Clase para extender las funcionalidades de la clase admin
class ServiceAdmin(admin.ModelAdmin):
    # Mostrar campos de solo lectura en el panel de administracion de django
    readonly_fields = ('created', 'updated')


# Register your models here.
admin.site.register(Service, ServiceAdmin)