from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidos = models.CharField(max_length = 100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length = 12)
    email = models.EmailField()
    domicilio = models.TextField()
    