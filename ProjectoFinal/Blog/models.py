from django.db import models


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profecion = models.CharField(max_length=50)


def __str__(self):
    return f"{self.nombre} {self.apellido}"


class secciones(models.Model):
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
