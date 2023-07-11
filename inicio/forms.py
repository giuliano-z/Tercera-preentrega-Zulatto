from django import forms
from inicio.models import Autor, Editorial, Libro

class CrearAutorFormulario(forms.Form): 
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)

class CrearEditorialFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=100)

class CrearLibroFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    editorial = forms.CharField(max_length=50)

class BusquedaFormulario(forms.Form):
    titulo = forms.CharField(max_length=100, required=False)