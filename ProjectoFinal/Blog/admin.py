from django.contrib import admin
from Blog.models import Articulo, Autor, Seccion, Blog, Avatar

admin.site.register(Blog)
admin.site.register(Articulo)
admin.site.register(Seccion)
admin.site.register(Autor)
admin.site.register(Avatar)
