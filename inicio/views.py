from inicio.forms import CrearAutorFormulario, CrearEditorialFormulario, CrearLibroFormulario, BusquedaFormulario
from inicio.models import Libro, Autor, Editorial
from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_autor(request):
    mensaje = 'El autor se creo correctamente'
    if request.method == 'POST':
        formularioA = CrearAutorFormulario(request.POST)
        if formularioA.is_valid():
            info = formularioA.cleaned_data
            autor = Autor(nombre = info ['nombre'], apellido = info ['apellido'])
            autor.save()
            mensajeA = f'Se creo el autor {autor.nombre}'
        else:
            return render(request, 'inicio/crear_autor.html', {'formularioA': formularioA, 'mensajeA': mensajeA})
    formularioA = CrearAutorFormulario()
    return render(request, 'inicio/crear_autor.html', {'formularioA': formularioA, 'mensaje': mensaje})

def crear_editorial(request):
    mensaje = 'La editorial se creo correctamente'
    if request.method == 'POST':
        formularioE = CrearEditorialFormulario(request.POST)
        if formularioE.is_valid():
            info = formularioE.cleaned_data
            editorial = Editorial(nombre = info ['nombre'], direccion = info ['direccion'])
            editorial.save()
            mensajeE = f'Se creo la editorial {editorial.nombre}'
        else:
            return render(request, 'inicio/crear_editorial.html', {'formularioE': formularioE, 'mensajeE': mensajeE})
    formularioE = CrearEditorialFormulario()
    return render(request, 'inicio/crear_editorial.html', {'formularioE': formularioE, 'mensaje': mensaje})

def crear_libro(request):
    mensaje = 'El libro se creo correctamente'
    if request.method == 'POST':
        formularioL = CrearLibroFormulario(request.POST)
        if formularioL.is_valid():
            info = formularioL.cleaned_data
            libro = Libro(titulo = info ['titulo'], autor = info ['autor'], editorial = info ['editorial'])
            libro.save()
            mensajeL = f'Se creo el libro {libro.titulo}'
        else:    
            return render(request, 'inicio/crear_libro.html', {'formularioL': formularioL, 'mensajeL': mensajeL})
    formularioL = CrearLibroFormulario()
    return render(request, 'inicio/crear_libro.html', {'formularioL': formularioL, 'mensaje': mensaje})

def lista_libros(request):
    formularioB = BusquedaFormulario()
    libros = None
    if request.method == 'POST':
        formularioB = BusquedaFormulario(request.POST)
        if formularioB.is_valid():
            busqueda = formularioB.cleaned_data['busqueda']
            libros = Libro.objects.filter(titulo__icontains=busqueda)

    return render(request, 'inicio/lista_libros.html', {'formularioB': formularioB, 'libros': libros})
