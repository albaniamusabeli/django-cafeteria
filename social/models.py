from django.db import models

# Create your models here.
class Link(models.Model):
    ## campo Slug --> para caracteres alfanumericos, guiones y slash. No permite espacios ni caracteres especiales
    key = models.SlugField(max_length=100, unique=True, verbose_name="Nombre clave")
    name = models.CharField(max_length=200, verbose_name="Red Social")
    url = models.URLField(max_length=200, verbose_name="Enlace", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'

        
        ordering = ['name']

    def __str__(self):
        return self.name