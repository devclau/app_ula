from django.db import models

# Create your models here.
class Notificacion(models.Model):
    date = models.DateField(verbose_name="Fecha")
    time = models.TimeField(verbose_name="Hora")
    link = models.URLField(verbose_name="URL")
    title = models.CharField(max_length=200,verbose_name="Titulo")
    detail = models.TextField(verbose_name="Mensaje")

    def __str__(self):
        return self.title
