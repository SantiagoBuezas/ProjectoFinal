from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from Blog.models import Blog, Autor, Articulo, Seccion
from Blog.forms import AutorForm, SeccionForm, ArticuloForm, BlogForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def mostrar_inicio(request):
    return render(request, "Blog/inicio.html")


@login_required
def mostrar_about(request):
    return render(request, "Blog/about.html")


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


@login_required
def busqueda_2(request):
    return render(request, "Blog/busqueda_2.html")


@login_required
def buscar_2(request):

    if not request.GET["tema"]:
        return HttpResponse("No enviaste datos")
    else:
        tema_a_buscar = request.GET["tema"]
        blogs = Blog.objects.filter(tema=tema_a_buscar)

        contexto = {"tema": tema_a_buscar, "blog_encontrados": blogs}

        return render(request, "Blog/resultado_busqueda.html", contexto)


class BlogsList(ListView, LoginRequiredMixin):

    model = Blog
    template_name = "Blog/blogs-list.html"


class BlogDetalle(DetailView, LoginRequiredMixin):

    model = Blog
    template_name = "Blog/blog-detalle.html"


class BlogCreacion(CreateView, LoginRequiredMixin):
    model = Blog
    fields = ["nombre", "tema"]

    def get_success_url(self):
        return reverse("BlogList")


class BlogUpdateView(UpdateView, LoginRequiredMixin):
    model = Blog
    fields = ["nombre", "tema"]

    def get_success_url(self):
        return reverse("BlogList")


class BlogDelete(DeleteView, LoginRequiredMixin):
    model = Blog

    def get_success_url(self):
        return reverse("BlogList")


class MyLogin(LoginView):
    template_name = "Blog/login.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()

            return render(
                request,
                "Blog/inicio.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "Blog/register.html", {"form": form})
    
class MyLogout(LogoutView, LoginRequiredMixin):
    template_name = "Blog/logout.html"