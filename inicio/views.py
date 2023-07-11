from inicio.forms import CrearAutorFormulario, CrearEditorialFormulario, CrearLibroFormulario, BusquedaFormulario
from inicio.models import Libro, Autor, Editorial
from django.shortcuts import render, redirect

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_autor(request):
    if request.method == 'POST':
        formularioA = CrearAutorFormulario(request.POST)
        if formularioA.is_valid():
            info = formularioA.cleaned_data
            autor = Autor(nombre = info ['nombre'], apellido = info ['apellido'])
            autor.save()
        else:
            return render(request, 'inicio/crear_autor.html', {'formularioA': formularioA})
    formularioA = CrearAutorFormulario()
    return render(request, 'inicio/crear_autor.html', {'formularioA': formularioA})

def crear_editorial(request):
    if request.method == 'POST':
        formularioE = CrearEditorialFormulario(request.POST)
        if formularioE.is_valid():
            info = formularioE.cleaned_data
            editorial = Editorial(nombre = info ['nombre'], direccion = info ['direccion'])
            editorial.save()
        else:
            return render(request, 'inicio/crear_editorial.html', {'formularioE': formularioE})
    formularioE = CrearEditorialFormulario()
    return render(request, 'inicio/crear_editorial.html', {'formularioE': formularioE})

def crear_libro(request):
    if request.method == 'POST':
        formularioL = CrearLibroFormulario(request.POST)
        if formularioL.is_valid():
            info = formularioL.cleaned_data
            libro = Libro(titulo = info ['titulo'], autor = info ['autor'], editorial = info ['editorial'])
            libro.save()
            return redirect('inicio:lista_libros')
        else:    
            return render(request, 'inicio/crear_libro.html', {'formularioL': formularioL})
    
    formularioL = CrearLibroFormulario()
    return render(request, 'inicio/crear_libro.html', {'formularioL': formularioL})

def lista_libros(request): 
    formulario = BusquedaFormulario(request.GET)
    if formulario.is_valid():
        busqueda = formulario.cleaned_data['titulo']
        lista_libros = Libro.objects.filter(titulo__icontains=busqueda)
    formulario = BusquedaFormulario()
    return render(request, 'inicio/lista_libros.html', {'formulario':formulario, 'libros':lista_libros})

