from django import forms


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
