from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from Blog.forms import AutorForm, SeccionForm, ArticuloForm, BlogForm


def mostrar_inicio(request):
    return render(request, "Blog/inicio.html")


def procesar_formulario_blog(request):
    mi_formulario = BlogForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "Blog/formulario-blog.html", context=contexto)


def procesar_formulario_autor(request):
    mi_formulario = AutorForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "Blog/formulario-autor.html", context=contexto)


def procesar_formulario_seccion(request):
    mi_formulario = SeccionForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", context=contexto)


def procesar_formulario_articulo(request):
    mi_formulario = ArticuloForm()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-articulo.html", context=contexto)
