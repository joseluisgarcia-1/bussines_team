from django.db import models

# Create your models here.
class Mascota(models.Model):
    folio = models.CharField(max_length = 50, primary_key = True)
    nombre = models.CharField(max_length = 500)
    sexo = models.CharField(max_length = 50)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()