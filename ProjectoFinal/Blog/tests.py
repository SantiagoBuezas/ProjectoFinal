from django.test import TestCase
from Blog.models import Blog


class ViewTestCase(TestCase):
    def test_tema_de_blog(self):
        Blog.objects.create(nombre="Camino de Pena", tema="Warhammer")
        todos_los_blog = Blog.objects.all()
        assert len(todos_los_blog) == 1
        assert todos_los_blog[0].tema == "Warhammer"

    def test_fecha_de_blog(self):
        Blog.objects.create(
            nombre="El Hobbit", tema="El señor de los anillos", fecha="10/10/2021"
        )
        todos_los_blog = Blog.objects.all()
        assert todos_los_blog[0].fecha_de_inicio != None

    def test_crear_4_blog(self):
        Blog.objects.create(nombre="Camino a la Gloria", tema="Warhammer")
        Blog.objects.create(nombre="Camino a la muerte", tema="Warhammer")
        Blog.objects.create(nombre="La comunidad del anillo", tema="ESDA")
        Blog.objects.create(nombre="las dos torres", tema="ESDA")
        Blog.objects.create(nombre="El retorno del Rey", tema="ESDA")
        todos_los_blogs = Blog.objects.all()
        assert len(todos_los_blogs) == 4
