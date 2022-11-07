from django.contrib import admin
from django.urls import path, include

from Blog.views import (
    mostrar_inicio,
    procesar_formulario_blog,
    procesar_formulario_autor,
    procesar_formulario_seccion,
    procesar_formulario_articulo,
    busqueda_2,
    buscar_2,
    BlogsList,
    BlogDetalle,
    BlogCreacion,
    BlogUpdateView,
    BlogDelete,
    mostrar_about,
    MyLogin,
    register,
    MyLogout,
    editar_perfil,
)

urlpatterns = [
    path("inicio/", mostrar_inicio, name="inicio"),
    path("formulario-blog/", procesar_formulario_blog, name="formulario-blog"),
    path("formulario-autor/", procesar_formulario_autor, name="formulario-autor"),
    path("formulario-seccion/", procesar_formulario_seccion, name="formulario-seccion"),
    path(
        "formulario-articulo/", procesar_formulario_articulo, name="formualrio-articulo"
    ),
    path("busqueda-2/", busqueda_2, name="busqueda-2"),
    path("buscar-2/", buscar_2, name="bucar-2"),
    path("blogs-list/", BlogsList.as_view(), name="BlogList"),
    path("r'(?P<pk>\d+)^$'", BlogDetalle.as_view(), name="BlogDetail"),
    path("blog-nuevo/", BlogCreacion.as_view(), name="BlogNew"),
    path("editar/<pk>", BlogUpdateView.as_view(), name="BlogUpdate"),
    path("borrar/<pk>", BlogDelete.as_view(), name="BlogDelete"),
    path("about/", mostrar_about, name="About-me"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("register/", register, name="Register"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("editar-perfil/", editar_perfil, name="EditarPerfil"),
]
