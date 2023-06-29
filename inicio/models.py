from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)


