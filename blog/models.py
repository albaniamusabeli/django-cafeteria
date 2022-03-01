from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length=100, verbose_name="Nombre")
    created     = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated     = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

        #ordenar por fecha de creacion (el signo - ordena desde el mas nuevo al mas viejo)
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title       = models.CharField(max_length=200, verbose_name="Titulo")
    content     = models.TextField(verbose_name="Contenido")
    published   = models.DateTimeField(verbose_name='Fecha de Publicación', default=now)
    image       = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name='Imagen')
    # Author es foraneo.. en caso de borrarlo se borrará en cascada.. o sea tambien borrará los blogs que
    # el autor haga
    author      = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories  = models.ManyToManyField(Category, verbose_name='Categorias', related_name="get_posts")

    created     = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated     = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

        #ordenar por fecha de creacion (el signo - ordena desde el mas nuevo al mas viejo)
        ordering = ['-created']

    def __str__(self):
        return self.title