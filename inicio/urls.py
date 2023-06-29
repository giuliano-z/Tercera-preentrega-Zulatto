from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/autor', views.crear_autor, name='crear_autor'),
    path('crear/editorial', views.crear_editorial, name='crear_editorial'),
    path('crear/libro', views.crear_libro, name='crear_libro')
]