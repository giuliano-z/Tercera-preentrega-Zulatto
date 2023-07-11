from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/autor', views.crear_autor, name='crear_autor'),
    path('crear/editorial', views.crear_editorial, name='crear_editorial'),
    path('libro/crear', views.crear_libro, name='crear_libro'),
    path('inicio/lista_libros', views.lista_libros, name='lista_libros')
]