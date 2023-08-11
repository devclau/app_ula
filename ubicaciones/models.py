from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_cat = models.IntegerField( primary_key=True )
    tipo_cat = models.CharField( blank=True, null=True, max_length=50)
    nom_cat = models.CharField( blank=True, null=True, max_length=50)
    def __str__(self):
        return self.nom_cat

class Dependencia(models.Model):
    id_dep = models.IntegerField( blank=True, null=True)
    nom_dep = models.CharField(max_length=50)
    id_acceso = models.IntegerField( blank=True, null=True)
    id_edif = models.IntegerField( blank=True, null=True)
    id_sede = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='dependencias', db_column='id_sede', to_field='id_cat')
    id_dire = models.IntegerField( blank=True, null=True)
    id_ciud = models.IntegerField( blank=True, null=True)
    longitud = models.CharField(max_length=50)
    latitud = models.CharField(max_length=50)
    def __str__(self):
        return self.nom_dep

class Espacio(models.Model):
    id_espc = models.IntegerField( blank=True, null=True)
    nom_espc = models.CharField( blank=True, null=True, max_length=50)
    id_esp = models.IntegerField( blank=True, null=True)
    id_func = models.IntegerField( blank=True, null=True)
    id_usab = models.IntegerField( blank=True, null=True)
    id_usua = models.IntegerField( blank=True, null=True)
    id_nivel = models.IntegerField( blank=True, null=True)
    id_dep = models.ForeignKey(Dependencia, on_delete=models.CASCADE, related_name='espacios', db_column='id_dep')

    def __str__(self):
        return self.nom_espc