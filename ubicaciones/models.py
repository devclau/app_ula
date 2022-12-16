from django.db import models

# Create your models here.

class Sede(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self)-> str:
        return self.nombre
    
    class Meta:
        db_table = 'sede'
        verbose_name='Sede'
        verbose_name_plural='Sedes'


class Reparticion(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.TextField(null=True, blank=False )

    class Meta:
        db_table = 'reparticion'
        verbose_name= 'reparticion'
        verbose_name_plural='reparciones'

    def __str__(self) -> str:
        return self.nombre

#TABLA PIVOTE SEDE-REPARTICIONES 

class SedeRaparticion(models.Model):
    sede = models.ForeignKey(Sede, models.DO_NOTHING, null=False)
    reparticion = models.ForeignKey(Reparticion, models.DO_NOTHING, null=False)
    
    def __str__(self):
        return f"{self.sede} - {self.reparticion}"

class Espacio(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    imagen = models.CharField(max_length=200, null=True, blank=True)
    coordenadas = models.CharField(max_length=250, null=False, blank=False)

    class Meta:
        db_table = 'espacio'
        verbose_name= 'Espacio'
        verbose_name_plural = 'Espacios'

    def __str__(self):
        return self.nombre



class Uso(models.Model):
    nombre = nombre = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'uso'
        verbose_name = 'Uso'
        verbose_name_plural = 'Usos'

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True, default='null')

    class Meta:
        db_table = 'servicio'
        verbose_name = 'Servicio'
        verbose_name_plural ='Servicios'

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    fonos = models.CharField(max_length=100, null=True, blank=True)
    web = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    otro = models.TextField()
    horarios =  models.CharField(max_length=100, null=True, blank=True)
    personas= models.TextField()

    def __str__(self):
            return f"{self.fonos} - {self.web}"


#TABLA PIVOTE REPARTICION - ESPACIO 
class ReparticionEspacio(models.Model):
    reparticion_sede = models.ForeignKey(SedeRaparticion, models.DO_NOTHING, null=True)
    espacio = models.ForeignKey(Espacio, models.DO_NOTHING, null=True)
    contacto = models.ForeignKey(Contacto, models.DO_NOTHING, null=True)
    uso = models.ForeignKey(Uso, models.DO_NOTHING, null=True)
    servicio = models.ForeignKey(Servicio, models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.reparticion_sede} - {self.espacio}"