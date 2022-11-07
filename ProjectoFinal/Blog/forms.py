from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    tema = forms.CharField(max_length=50)
    fecha = forms.DateField()


class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=50)


class ArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    texto = forms.CharField(max_length=1000)
    fecha = forms.DateField()


class SeccionForm(forms.Form):
    nombre = forms.CharField(max_length=50)


class UserEditionForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Primer Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        # help_texts = {k: "" for k in fields}
