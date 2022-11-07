from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from Blog.models import Blog, Autor, Articulo, Seccion, Avatar
from Blog.forms import (
    AutorForm,
    SeccionForm,
    ArticuloForm,
    BlogForm,
    UserEditionForm,
    AvatarForm,
    MensajeForm,
)
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


@login_required
def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "Blog/inicio.html", contexto)


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
    if request.method == "POST":
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


class BlogsList(LoginRequiredMixin, ListView):

    model = Blog
    template_name = "Blog/blogs-list.html"


class BlogDetalle(LoginRequiredMixin, DetailView):

    model = Blog
    template_name = "Blog/blog-detalle.html"


class BlogCreacion(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ["nombre", "tema"]

    def get_success_url(self):
        return reverse("BlogList")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ["nombre", "tema"]

    def get_success_url(self):
        return reverse("BlogList")


class BlogDelete(LoginRequiredMixin, DeleteView):
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
                "Blog/post-register.html",
                {"mensaje": f"Usuario: {username_capturado}"},
            )

    else:
        form = UserCreationForm()

    return render(request, "Blog/register.html", {"form": form})


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "Blog/logout.html"


@login_required
def editar_perfil(request):
    user = request.user
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "Blog/inicio.html")

    contexto = {
        "user": user,
        "form": form,
    }
    return render(request, "Blog/editarPerfil.html", contexto)


@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "Blog/inicio.html")

    contexto = {"form": form}
    return render(request, "Blog/avatar_form.html", contexto)


def mandar_mensaje(request):
    if request.method == "GET":
        mi_formulario = MensajeForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-de-mensajes.html", context=contexto)
    if request.method == "POST":
        return render(request, "blog/mensaje-enviado.html")


def mensaje_enviado(request):
    return render(request, "blog/mensaje-enviado.html")
