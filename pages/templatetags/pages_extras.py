from django import template
from pages.models import Page


register = template.Library()

@register.simple_tag
def obtener_lista_paginas():
    ## obtener todas las paginas de la bbdd
    pages = Page.objects.all()
    return pages