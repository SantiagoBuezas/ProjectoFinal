from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    class Meta:
        verbose_name_plural = "Blogs"

    nombre = models.CharField(max_length=50)
    tema = models.CharField(max_length=50)
    fecha = models.DateField(null=True)
    cuerpo = models.CharField(max_length=1000, null=True)
    autor_nombre_completo = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.tema})"


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"


class Articulo(models.Model):
    class Meta:
        verbose_name_plural = "Articulos"

    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null=True)

    def __str__(self):
        return f"{self.titulo} ({self.fecha})"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


class Mensaje(models.Model):

    email = models.EmailField()
    texto = models.CharField(max_length=1000)
