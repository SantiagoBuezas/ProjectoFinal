from django.contrib import admin
from django.urls import path, include

from Blog.views import (
    mostrar_inicio,
    procesar_formulario_blog,
    procesar_formulario_autor,
    procesar_formulario_seccion,
    procesar_formulario_articulo,
)

urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario-blog/", procesar_formulario_blog),
    path("formulario-autor/", procesar_formulario_autor),
    path("formulario-seccion/", procesar_formulario_seccion),
    path("formulario-articulo/", procesar_formulario_articulo),
]
