from django.db import models

# Create your models here.

class Sede(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False,verbose_name='Nombre Sede')
    
    def __str__(self)-> str:
        return self.nombre

    class Meta:
        db_table = 'sede'
        verbose_name='Sede'
        verbose_name_plural='Sedes'


class Reparticion(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.TextField(null=True, blank=False )
    ciudad  = models.CharField(max_length=100)

    class Meta:
        db_table = 'reparticion'
        verbose_name= 'reparticion'
        verbose_name_plural='reparciones'

    def __str__(self) -> str:
        return self.nombre



class Espacio(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    imagen = models.CharField(max_length=200, null=True, blank=True,help_text='Imagen URL')
    coordenadas = models.CharField(max_length=250, null=False, blank=False, help_text='Coordenadas (Longitud , Latitud)')
    uso = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'espacio'
        verbose_name= 'Espacios'
        verbose_name_plural = 'Espacios'

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
    personas= models.TextField(help_text='Personas (nombre,cargo, email,fonos)')
    

    def __str__(self):
            return f"{self.fonos} - {self.web}"


############################################################################################



class DiaSemana(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Dia de la Semana')

    def __str__(self):
        return self.nombre





#TABLA PIVOTE SEDE-REPARTICIONES #### TABLA PRINCIPAL

class SedeRaparticion(models.Model):
    sede = models.ForeignKey(Sede, models.CASCADE, null=True)
    reparticion = models.ForeignKey(Reparticion, models.CASCADE, null=True)
    espacio = models.ForeignKey(Espacio, models.CASCADE, null=True)
    servicio = models.ForeignKey(Servicio, models.CASCADE, null=True)
    contacto = models.ForeignKey(Contacto, models.CASCADE, null=True)
    diahoras = models.ManyToManyField(DiaSemana,through='DiasHora', blank=True,)
    def __str__(self):
        return f"{self.sede} - {self.reparticion}"

    class Meta:
        verbose_name = "Formulario de Ingreso"

############################################################################################

class DiasHora(models.Model):
    
   
    diasemamna = models.ForeignKey(
        DiaSemana, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    reparticionEspacio = models.ForeignKey(
        SedeRaparticion, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    hora = models.CharField(max_length=100, null=True, blank=True)