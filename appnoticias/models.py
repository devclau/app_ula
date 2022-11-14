from django.db import models

# Create your models here.

class Pfrecuente(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    respuesta = models.TextField()