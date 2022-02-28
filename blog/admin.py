from django.contrib import admin
from .models import Category, Post

# Register your models here.
# Clase para extender las funcionalidades de la clase 
class CategoryAdmin(admin.ModelAdmin):
    # Mostrar campos de solo lectura en el panel de administracion de django
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)


# Clase para extender las funcionalidades de la clase 
class PostAdmin(admin.ModelAdmin):
    # Mostrar campos de solo lectura en el panel de administracion de django
    readonly_fields = ('created', 'updated')

    # agregar nuevas columnas al panel de administracion de django
    list_display = ('title', 'author', 'published', 'post_categories')

    ordering = ('author', 'published')

    ## Mostrar formulario de busqueda/ Puedes buscar por la tabla autor con el username de autor, 
    # lo mismo la tabla categorias
    search_fields = ('title', 'author__username', 'categories__name')

    # en campos DateTime se puede filtrar por fecha
    date_hierarchy = 'published'

    # FILTRAR POR CAMPOS RELACIONADOS
    list_filter = ('author__username', 'categories')

    
    ## Metodo para crear nuestros propios campos y mostrarlos como columnas en el panel admin
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    ## Sobrescribir el nombre de la funcion post_categories
    post_categories.short_description = "Categorias"


admin.site.register(Post, PostAdmin)
