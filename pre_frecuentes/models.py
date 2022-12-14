from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural='Categorias'


class Pregunta(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    respuesta = models.TextField()
    categoria = models.ForeignKey(Categoria,  models.DO_NOTHING, null=True)
    
    
    def __str__(self) -> str:
        return self.titulo

    def dic_preguntas(self):
        return {
            
            'titulo': self.titulo,
            'respuesta':self.respuesta
        }

    class Meta:
        db_table = 'preguntas'
        verbose_name = 'Pregunta'
        verbose_name_plural='Preguntas'


