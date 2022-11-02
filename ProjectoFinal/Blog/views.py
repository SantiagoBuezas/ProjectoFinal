from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from Blog.models import Blog, Autor, Articulo, Seccion
from Blog.forms import AutorForm, SeccionForm, ArticuloForm, BlogForm


def mostrar_inicio(request):
    return render(request, "Blog/inicio.html")


def procesar_formulario_blog(request):
    if request.method == "GET":
        mi_formulario = BlogForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-blog.html", context=contexto)

    if request.method == "POST":
        mi_formulario = BlogForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Blog(
                nombre=datos_ingresados_por_usuario["nombre"],
                tema=datos_ingresados_por_usuario["tema"],
                fecha=datos_ingresados_por_usuario["fecha"],
            )
            nuevo_modelo.save()

        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-blog.html", context=contexto)


def procesar_formulario_autor(request):
    if request.method == "GET":
        mi_formulario = AutorForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-autor.html", context=contexto)
    if request.method == "POST":
        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                profesion=datos_ingresados_por_usuario["profesion"],
            )
            nuevo_modelo.save()
        contexto = {"formulario": mi_formulario}
        return render(request, "Blog/formulario-autor.html", context=contexto)


def procesar_formulario_seccion(request):
    if request.method == "GET":
        mi_formulario = SeccionForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-seccion.html", context=contexto)
    if request.method == "POST":
        mi_formulario = SeccionForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Seccion(nombre=datos_ingresados_por_usuario["nombre"])
            nuevo_modelo.save()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", context=contexto)


def procesar_formulario_articulo(request):
    if request.method == "GET":
        mi_formulario = ArticuloForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-articulo.html", context=contexto)
    if request.method == "PSOT":
        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo=datos_ingresados_por_usuario["titulo"],
                texto=datos_ingresados_por_usuario["texto"],
                fecha=datos_ingresados_por_usuario["fecha"],
            )
            nuevo_modelo.save()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-articulo.html", context=contexto)
