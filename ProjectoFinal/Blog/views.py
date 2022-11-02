from django.http import HttpResponse
from django.shortcuts import render

def mostrar_inicio(request):
    return render(request, "Blog/inicio.html")
